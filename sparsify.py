__author__ = 'xiaofeng'
from graph_models import *
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
from igraph import *
import math
import random

const = 10

#input graph is unweighted, epsilon is the error rate
#return a combinatorial sparsified graph preserving cut size
#Loop simply for edges
def spars_combi_naive(G, epsilon):

    N = G.vcount()
    rho = 0.001 * (math.log(N, 10)) * (math.log(N, 10))/(epsilon * epsilon) #A smaller constant?
    H = G


    for edge in G.get_edgelist():
#        H.delete_edges(edge)
        #adhersion is the same method as edge_disjoint_paths  "...get_all_shortest_paths"
        # and parallel over nodes

        lamda_connectivity = G.adhesion(edge[0], edge[1], checks = True) + 1
        #This edge connectivity will grow really fast when node number N grows
        #lpus one for singletons
        p_e = rho/lamda_connectivity
        random_var = random.random()
        if random_var < p_e:
#            w = 1/p_e
#            H.add_edge(edge[0], edge[1], weight = w)
            pass
        else:
            H.delete_edges(edge)


    return H

#Gomory-Hu:
# Loop For each node all pair max flow
def spars_combi(G, epsilon):

    N = G.vcount()
    rho = 1.0 * (math.log(N, 10)) * (math.log(N, 10))/(epsilon * epsilon)
    H = G  #is it the same copy??

    ##########for edge connectivity run dijkstra once and have a value for all nodes, instead of too much G.adhesion
    ##########parallel the construction of gomory_hu_tree on spark later
    #########  for node in G.vs["name"]:
    T = G.gomory_hu_tree()



    for edge in G.get_edgelist():

        H.delete_edges(edge)

        #parallel over nodes
        list_of_eid = T.get_shortest_paths(edge[0], to = edge[1], output = "epath")  #[[3, 4]]
        min_w = 9999
        for path in list_of_eid:
            for e in path:
                if T.es[e]["flow"] < min_w:
                    min_w = T.es[e]["flow"]
       # print min_w

        lamda_connectivity = min_w + 1
        #This edge connectivity will grow really fast when node number N grows
        #lpus one for singletons
        p_e = rho/lamda_connectivity/const
#        print "P_e = "
#        print p_e
        random_var = random.random()
        if random_var < p_e:
            w = 1/p_e
            H.add_edge(edge[0], edge[1], weight = w)
        else:
            print "____________go to egde discarding__________________"
  #  print "_________AFTER:__________"
  #  print H
    return H
