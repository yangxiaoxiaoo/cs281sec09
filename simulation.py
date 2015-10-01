import demo
import sparsify
from graph_models import *
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
import pickle
from igraph import *
import graph_statistics
import networkx as nx

def Gen_probMatrix_from_PQ(p, q, R):
    d = []
    for i in range(0,R):
        d.append([p]* R)
        d[i][i] = q
    return d

def Gen_SBM(p, q, N, R):
    #igraph version with SBM is only available on mac
    block_size_list = []
    #create a list of block sizes with equal sizes
    for i in range(0,R):
        block_size_list.append(N/R)
    B = Gen_probMatrix_from_PQ(p, q, R)
    a= Graph.SBM(N,B,block_size_list)
    return a

def RealSim():

    GraphName = "MontereyBay"

    def Expand(GraphName):
        #finish the expending process in Networkx and write back to an adjacency list file
        G = nx.read_adjlist(GraphName +"_list.txt")

        return G

    SBM_1 = Graph.Read_Ncol(GraphName +"_list.txt", directed=False)
    Expand(GraphName)
    SBM_expanded = Graph.Read_Ncol(GraphName+"_expanded.txt", directed=False)

    dict1 = graph_statistics.regular_stat(SBM_1)
    SBM_2 = sparsify.spars_combi(SBM_1, epsilon=0.5)
   #
   # dict1 = graph_statistics.regular_stat(SBM_1)
    dict2 = graph_statistics.regular_stat(SBM_2)
    for key in dict1:
        print key + ":"+ str(dict1[key])+"=>" + str(dict2[key])

def simulate():

    N = 100
    R = 5
    b1 = 1.5
    b0 = 0.5
    a  = 1.0
    alpha0 = a*np.ones(R)
    SBM_1 = StochasticBlockModel(R, b0, b1, alpha0)
    (A,f,theta) = sample_network(SBM_1,N)
    (B, pi) = theta


    p = 0.3
    q = 0.7
    N = 100
    R = 5

    ####run once on mac for picked SBM data
    ####start-----------pickle string won't keep the graph
    graph_1 = Gen_SBM(p, q, N, R)
    print graph_1
    Graph.write_pickle(graph_1,"SBM_03_07_1000_5.p")
    ####end-------------

    SBM_1 = Graph.Read_Pickle("SBM_03_07_1000_5.p")
    SBM_2 = sparsify.spars_combi(SBM_1, epsilon=0.5)

'''


    def invariant_order(f):
        """
        Return an (almost) invariant ordering of the block labels
        """
        # Cast features to block IDs
        z = np.array(f).astype(np.int)
        # Create a copy
        zc = np.copy(z)
        # Sort block IDs according to block size
        M = np.zeros(R)
        for r in np.arange(R):
            M[r] = np.sum(z==r)
        # Sort by size to get new IDs
        newz = np.argsort(M)
        # Update labels in zc
        for r in np.arange(R):
            zc[z==newz[r]]=r
        return np.argsort(-zc)

    # Generate a test network or use a given network
    plt.figure()

    if True:
        (A,f,theta) = sample_network(SBM_1,N)
        zs = invariant_order(f)
        plt.subplot(1,3,1)
        plt.spy(A[np.ix_(zs,zs)])
        plt.title("before")

        (A,f,theta) = sample_network(SBM_2,N)
        zs = invariant_order(f)
        plt.subplot(1,3,3)
        plt.spy(A[np.ix_(zs,zs)])
        plt.title("after")

    plt.show()
'''
if __name__ == "__main__":
  #  simulate()
    RealSim()
