__author__ = 'xiaofeng'
from graph_models import *
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
from igraph import *
import math

#input graph is unweighted, epsilon is the error rate
#return a combinatorial sparsified graph preserving cut size
def spars(G, epsilon):

    N = G.vcount()
    rho = 1.0 * (math.log(N, 2))^2 /(epsilon^2)
   # H = enpty...
    for edge in G.get_edgelist():
        #adhersion is the same method as edge_disjoint_paths
        lamda_connectivity = G.adhesion(edge[0], edge[1], checks = True)
        p = rho/lamda_connectivity
     #   H.add ...


    return G #H