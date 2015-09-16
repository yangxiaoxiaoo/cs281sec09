__author__ = 'xiaofeng'
from graph_models import *
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
from igraph import *
import math
import random

#input graph is unweighted, epsilon is the error rate
#return a combinatorial sparsified graph preserving cut size
def spars_combi(G, epsilon):

    N = G.vcount()
    rho = 1.0 * (math.log(N, 2)) * (math.log(N, 2))/(epsilon * epsilon)
    H = G

    for edge in G.get_edgelist():
        H.delete_edges(edge)
        #adhersion is the same method as edge_disjoint_paths
        lamda_connectivity = G.adhesion(edge[0], edge[1], checks = True) + 1
        #This edge connectivity will grow really fast when node number N grows
        #lpus one for singletons
        p_e = rho/lamda_connectivity
        random_var = random.random()
        if random_var < p_e:
            w = 1/p_e
            H.add_edge(edge[0], edge[1], weight = w)

    return H