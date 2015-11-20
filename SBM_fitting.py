from graph_models import *
import networkx
import community
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
import igraph

'''
example::
A = np.asarray(np.matrix([[1., 1.], [1., 1.]]))
print type(A)
B = np.zeros((2,2))
print type(B)
'''

def decide_block_num(G,name):
    #community best partition -  louvain method
    partition = community.best_partition(G)
    sizes = list()
    for comm in set(partition.values()):
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == comm]
        size_com = len(list_nodes)
        sizes.append(size_com)

    sizes.sort()
    print sizes
    with open("blocksizes.txt", 'a') as fout:
        fout.write(str(name)+ ' ' + str(sizes))

def convert(inputf, outputf):
    #convert input an lgl to output an edgelist file
    with open(outputf, "w") as fout:
        with open(inputf, "r")as fin:
            s = 0
            for line in fin:
                if line[0] == '#':
                    s = int(line.split(' ')[1])
                else:
                    t = int(line)
                fout.write(str(s) + " " + str(t) + "\n")


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

    convert("/home/cbw/sbm/fb/Toronto_2008.lgl","Toronto_2008.ncol")
    decide_block_num(networkx.read_edgelist("Toronto_2008.ncol"),"Toronto2008")
 #   main()