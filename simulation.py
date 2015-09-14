import demo
import sparsify
from graph_models import *
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np
from igraph import *


def simulate():
    N = 10
    R = 5
    b1 = 1.5
    b0 = 0.5
    a  = 1.0
    alpha0 = a*np.ones(R)
    SBM_1 = StochasticBlockModel(R, b0, b1, alpha0)
    (A,f,theta) = sample_network(SBM_1,N)
    (B, pi) = theta
    aftersampled = Graph.Tree(127,2)
    a= Graph.SBM(N,B,R)

    print A
    print "________"
    print Graph.get_adjacency(aftersampled)
    SBM_2 = sparsify.spars(SBM_1, epsilon=0.05)




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

if __name__ == "__main__":
    simulate()