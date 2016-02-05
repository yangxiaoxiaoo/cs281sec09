#!/usr/bin/python
import subprocess
from pyspark import SparkContext
import json
import pickle
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import networkx as nx
import itertools


def deisomorphism(patternset):
    deisoed_set = set()
    for item in patternset:
        Unique = True
        for item2 in deisoed_set:
            if nx.is_isomorphic(item, item2):
                Unique = False
        if Unique:
            deisoed_set.add(item)
    return deisoed_set

def merge_nodes(G,node1,node2):
    if node1 in G and node2 in G:
        for neighbor in G.neighbors(node1):
            G.add_edge(neighbor, node2)
        G.remove_node(node1)
    return G

def patternsets2(MotifG1, MotifG2):
    #enumerate all possible permutations of node labels,
    #minimum is sharing one edge, all the way to max is the smaller number of edges, complexity 2^edgenum_max
    #return a set of possibly isomorphic collapses

    patternset = set()
    edgenum_max = min(MotifG1.number_of_edges(), MotifG2.number_of_edges())

    #select L (two+) edges to overlap
    for L in range(1, edgenum_max + 1):
        print L
        L_subsets = list(itertools.combinations(MotifG1.edges(),L))
        L_subsets2 = list(itertools.combinations(MotifG2.edges(),L))
        for subset1 in L_subsets:
            for subset2 in L_subsets2:
                print "already chose these" +str(L)+" edges in Motif2"
                print subset2
                permutations = list(itertools.permutations(subset1))
                i = 0
                for permutation in permutations:
                    print "this permutation is"
                    print permutation
                    print "in this particular order" + str(i)
                    if MotifG1 == MotifG2:
                        print "waring!!!same motif non-relabled"
                        G = nx.disjoint_union(MotifG1, MotifG2)
                    else:
                        G = nx.union(MotifG1, MotifG2)

                    if len(G) != 0:
                        G2 = nx.Graph()
                        G22 = nx.Graph()
                        Motif2merged_nodes = set()
                        for j in range(0, len(permutation)):
                            edge_1 = permutation[j]
                            edge_2 = subset2[j]
                            print "edge 1"
                            print edge_1
                            print "edge 2"
                            print edge_2

                            if edge_2[0] not in Motif2merged_nodes:
                                G1 = merge_nodes(G, edge_1[0], edge_2[0])
                                Motif2merged_nodes.add(edge_2[0])
                            if edge_2[1] not in Motif2merged_nodes:
                                G2 = merge_nodes(G1, edge_1[1], edge_2[1])
                                Motif2merged_nodes.add(edge_2[1])

                            if edge_2[0] not in Motif2merged_nodes:
                                G11 = merge_nodes(G, edge_1[1], edge_2[0])
                            if edge_2[1] not in Motif2merged_nodes:
                                G22 = merge_nodes(G11, edge_1[0], edge_2[1])

                        patternset.add(G2)
                        patternset.add(G22)
                        print G2.nodes()
                    i += 1


    return patternset

def three_hop(Graph):
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

    relations = 0
    for node in Graph.nodes():
        relations += len(hop3(Graph, node))
    return relations/2


def count_loss(Motif_pattern):
    loss = 0
    for edge in Motif_pattern.edges():
        before = three_hop(Motif_pattern)
        Motif_pattern.remove_edge(*edge)
        loss = before - three_hop(Motif_pattern)
        Motif_pattern.add_edge(*edge)
    return loss

def count_appearance(Motif_pattern, N, p):
    nodes_num = Motif_pattern.number_of_nodes()


def enumerate2():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7)

    G_2a  =nx.Graph()
    G_2a.add_edge(8, 9)
    G_2a.add_edge(9, 10)
    G_2a.add_edge(10, 11)
    G_2a.add_edge(11, 12)
    G_2a.add_edge(12, 8)

    G_2c = nx.Graph()
    G_2c.add_edge(13, 14)
    G_2c.add_edge(14, 15)
    G_2c.add_edge(13, 15)
    G_2c.add_edge(15, 16)

    G_3 = nx.Graph()
    G_3.add_edge(17, 18)
    G_3.add_edge(18, 19)
    G_3.add_edge(19, 20)
    G_3.add_edge(20, 21)
    G_3.add_edge(21, 22)
    G_3.add_edge(22, 17)

    #make sure theat all nodes have different names at this moment

    allpatterns = set()
    #Motifset = set([G_1a, G_1b, G_2a, G_2c, G_3])
    Motifset = set([G_1a, G_1b])
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            if not Motif1 == Motif2:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(Motif2.nodes())
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns.add(item)
    print len(allpatterns)
    return deisomorphism(allpatterns)

def enumerate3():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7)

    G_2a  =nx.Graph()
    G_2a.add_edge(8, 9)
    G_2a.add_edge(9, 10)
    G_2a.add_edge(10, 11)
    G_2a.add_edge(11, 12)
    G_2a.add_edge(12, 8)

    G_2c = nx.Graph()
    G_2c.add_edge(13, 14)
    G_2c.add_edge(14, 15)
    G_2c.add_edge(13, 15)
    G_2c.add_edge(15, 16)

    G_3 = nx.Graph()
    G_3.add_edge(17, 18)
    G_3.add_edge(18, 19)
    G_3.add_edge(19, 20)
    G_3.add_edge(20, 21)
    G_3.add_edge(21, 22)
    G_3.add_edge(22, 17)



    allpatterns = set()
    #Motifset = set([G_1a, G_1b, G_2a, G_2c, G_3])
    Motifset = set([G_1a, G_1b])
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            if len(set(Motif1.nodes()).intersection(Motif2.nodes())) == 0:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(max(Motif2.nodes()), max(Motif1.nodes()))
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns.add(item)
    print len(allpatterns)
    patterns_2 = deisomorphism(allpatterns)
    allpatterns_5_order = set()
    for Motif1 in patterns_2:
        for Motif2 in Motifset:
            if len(set(Motif1.nodes()).intersection(Motif2.nodes())) == 0:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns_5_order.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(max(Motif2.nodes()), max(Motif1.nodes()))
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns_5_order.add(item)
    return deisomorphism(allpatterns_5_order)

def main():
    #patterns = enumerate2()
    patterns = enumerate3()

if __name__ == "__main__":
    sc = SparkContext(appName="Sorted_removal")

    old_g = pickle.load(open("/net/data/facebook/facebook-ucsb/Facebook_2008/MontereyBay/original_pickles/MontereyBay.pickle", 'r'))
    new_g = nx.Graph()
    for node, friends in old_g.adj.iteritems():
        if node not in new_g.nodes():
            new_g.add_node(node)
        for friend in friends.iterkeys():
            new_g.add_node(friend)
            new_g.add_edge(node, friend)
#serialize the networkx graph as text files of edgelist
#into a text file for workers to read

 #   networkx.write_edgelist(new_g, "edgelist/MontereyBay", data=False)
 #   subprocess.check_call("hdfs dfs -put edgelist/MontereyBay edgelist/", shell=True)

    dataG = json_graph.node_link_data(new_g)
    stringG = json.dumps(dataG)
    originalG = sc.broadcast(stringG)
    edges = sc.textFile("hdfs://scrapper/user/xiaofeng/edgelist/MontereyBay")
    costs = edges.map(lambda line: line.split(' ')).map(lambda edge: edge_to_cost(edge, originalG.value))
    costs.saveAsTextFile("hdfs://scrapper/user/xiaofeng/costs_MontereyBay")
    sc.stop()
    subprocess.check_call("hdfs dfs -get costs_MontereyBay costs/", shell=True)
