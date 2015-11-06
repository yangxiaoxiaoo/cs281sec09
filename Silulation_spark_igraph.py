#!/usr/bin/python
#tailed from achtung ~/facebook/FacebookProject/spark_edgeremoval.py  - read from local edgelist instead

#using: spark-submit *this_file* Egypt 50

import igraph
import subprocess
from pyspark import SparkContext
import json
from networkx.readwrite import json_graph
import os, sys

def hop2(G, A):
    hop2_set = set()
    for neighbor in G.neighbors(A):
        hop2_set.add(neighbor)
        for neighbor2 in G.neighbors(neighbor):
            hop2_set.add(neighbor2)
    return hop2_set

def hop3(G, A):
    hop3_set = set()
    for neighbor in G.neighbors(A):
        hop3_set.add(neighbor)
        hop3_set = hop3_set.union(hop2(G, neighbor))
    return hop3_set

#sorted removal


def edge_to_cost(edge, G):
    #igraph edge , igraph graph object-> cost

    A = edge[0]
    B = edge[1]
    edge = (A, B)
    local_set = set(G.neighborhood(vertices=A, order=2)).union(set(G.neighborhood(vertices=B, order=2)))
    local_set.add(A)
    local_set.add(B)
    Ginterested = G.indeced_subgraph(vertices=local_set)
    hop3_before = 0
    for node in local_set:
        hop3_before += len(Ginterested.neighborhood(vertices=node, order=3))
    Ginterested.delete_edge(edge)
    hop3_after = 0
    for node in local_set:
        hop3_after += len(Ginterested.neighborhood(vertices=node, order=3))
    loss = (hop3_before - hop3_after)/2
    return edge, loss

def Reformat(path, name):
    #take a path of on disk spark-output files and convert into LGL file, put to current directory for later usage
    #tested
    dirs = os.listdir(path)
    with open(name + "_expanded_test.txt", 'w')as fout:
        for file in dirs:
            with open(path + file, 'r') as source:
                for line in source:
                    newline = line.replace('(', '').replace(')','').replace(',','')
                    fout.write(newline)


def main(name, divide):

    '''
    old_g = pickle.load(open("/net/data/facebook/facebook-ucsb/Facebook_2008/"+name +"/original_pickles/"+name +".pickle", 'r'))
    new_g = networkx.Graph()
    for node, friends in old_g.adj.iteritems():
        if node not in new_g.nodes():
            new_g.add_node(node)
        for friend in friends.iterkeys():
            new_g.add_node(friend)
            new_g.add_edge(node, friend)
            '''
#serialize the networkx graph as text files of edgelist
#into a text file for workers to read

 #   networkx.write_edgelist(new_g, "edgelist/"+name, data=False)
 #   subprocess.check_call("hdfs dfs -put edgelist/"+name+ " edgelist/", shell=True)



    G = igraph.Read_Ncol(name +"_list.txt", directed=False)
    sc = SparkContext(appName="Sorted_removal")

    originalG = sc.broadcast(G)
    edges = sc.textFile("hdfs://scrapper/user/xiaofeng/edgelist/"+name, 192*4*int(divide))
    costs = edges.map(lambda line: line.split(' ')).map(lambda edge: edge_to_cost(edge, G.value))
    costs.saveAsTextFile("hdfs://scrapper/user/xiaofeng/costs_"+name)
    sc.stop()
    subprocess.check_call("hdfs dfs -get costs_" + name + " /home/xiaofeng/facebook/FacebookProject/costs/", shell=True)
    Reformat("/home/xiaofeng/facebook/FacebookProject/costs/costs_" + name +"/", name)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])