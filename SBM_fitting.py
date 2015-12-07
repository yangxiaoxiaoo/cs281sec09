from graph_models import *
import networkx
import matplotlib.pyplot as plt
from scipy import sparse
import scipy.special
import numpy as np
import sys
import Queue




'''
Using MCMC to fit SBM model parameters
usage: SBM_fitting.py Graphname blocksize
'''



def fit_blocks(R, A, Graphname):
    #the set is prior
    b1 = 0.5
    b0 = 0.5
    a  = 0.7#initial value of unified block membership


    alpha0 = a*np.ones(R)
    model = StochasticBlockModel(R, b0, b1, alpha0)
    #starting with a set of prior. --may choose them to accelerate converging

    f_trace, theta_trace, lp_trace = fit_network(A, model, x0=None, N_iter=3, callback=None, pause=False)

    fout = open("SBM_fit_all_3iter.txt", "a")
    fout.write(Graphname + ";; " + "theta_trace:" + str(theta_trace) + ";; lp_trace:" + str(lp_trace) + "\n")
    fout.close()


def main(Graphname, blocksize):
    #decepticons:
    G = networkx.read_edgelist("/home/xiaofeng/graph-models/realgraph/" + Graphname + ".ncol")

 #achtung only:   G = networkx.read_edgelist("/home/xiaofeng/facebook/sparsify/cs281sec09/" + Graphname + ".ncol")

  #  G = networkx.read_edgelist("./" + Graphname + ".ncol")
  #causing memeory error here, try sparse one
  #  matrix = networkx.to_numpy_matrix(G)

    matrix = networkx.to_scipy_sparse_matrix(G)
    print "allocating memory to matrix success"

 #   A = np.asarray(matrix)
    A = matrix
    print A.shape
    fit_blocks(int(blocksize), A, Graphname)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
   # main("Test", 3)