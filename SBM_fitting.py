from graph_models import *
import networkx
import matplotlib.pyplot as plt
import scipy
import scipy.special
import numpy as np

G = networkx.read_edgelist("MontereyBay_list.txt")
A = np.asarray(networkx.to_numpy_matrix(G))
print A.shape

'''
example::
A = np.asarray(np.matrix([[1., 1.], [1., 1.]]))
print type(A)
B = np.zeros((2,2))
print type(B)
'''

R = 10
b1 = 0.5
b0 = 0.5
a  = 0.7
alpha0 = a*np.ones(R)
model = StochasticBlockModel(R, b0, b1, alpha0)
#starting with a set of prior. --may choose them to accelerate converging

f_trace, theta_trace, lp_trace = fit_network(A, model, x0=None, N_iter=50, callback=None, pause=False)

fout = open("SBM_fit_MontereyBay_10block.txt", "w")
fout.write(str(f_trace) + str(theta_trace) + str(lp_trace))
fout.close()
