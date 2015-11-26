from graph_models import *
import networkx
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np




'''
Using MCMC to fit SBM model parameters
only do fitting
'''



def fit_blocks(R, A):

    b1 = 0.5
    b0 = 0.5
    a  = 0.7
    alpha0 = a*np.ones(R)
    model = StochasticBlockModel(R, b0, b1, alpha0)
    #starting with a set of prior. --may choose them to accelerate converging

    f_trace, theta_trace, lp_trace = fit_network(A, model, x0=None, N_iter=50, callback=None, pause=False)

    fout = open("SBM_fit_MontereyBay_16blocks.txt", "a")
    fout.write( "R=" + str(R) +":" +str(f_trace) +" "+ str(theta_trace) +" "+ str(lp_trace) +"\n")
    fout.close()


def main():
    G = networkx.read_edgelist("MontereyBay_list.txt")
    A = np.asarray(networkx.to_numpy_matrix(G))
    print A.shape
 #   R = decide_block_num(G)
  #  fit_blocks(R)
    fit_blocks(16, A)





if __name__ == "__main__":

    main()