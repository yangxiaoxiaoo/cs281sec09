#!/usr/bin/python
#tailed from achtung ~/facebook/FacebookProject/spark_edgeremoval.py  - read from local edgelist instead

#using: spark-submit *this_file* Egypt 50


import igraph
import subprocess
from pyspark import SparkContext
import json
from networkx.readwrite import json_graph
import sys
import os, sys




def edge_to_cost(edge, G):
#edge : an igraph edge -> G : an igraph graph
    local_set = set(G.neighnorhood(order=3))


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


    new_g = networkx.read_adjlist(name +"_list.txt") #Egypt_list is an edge list
    sc = SparkContext(appName="Sorted_removal")

    dataG = json_graph.node_link_data(new_g)
    stringG = json.dumps(dataG)
    originalG = sc.broadcast(stringG)
    edges = sc.textFile("hdfs://scrapper/user/xiaofeng/edgelist/"+name, 192*4*int(divide))
    costs = edges.map(lambda line: line.split(' ')).map(lambda edge: edge_to_cost(edge, originalG.value))
    costs.saveAsTextFile("hdfs://scrapper/user/xiaofeng/costs_"+name)
    sc.stop()
    subprocess.check_call("hdfs dfs -get costs_" + name + " /home/xiaofeng/facebook/FacebookProject/costs/", shell=True)
    Reformat("/home/xiaofeng/facebook/FacebookProject/costs/costs_" + name +"/", name)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])