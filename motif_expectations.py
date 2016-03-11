#calculate an stimation occrance for all shapes in 5
import matplotlib.pyplot as plt
import numpy as np

def oracle_5(n, p):
    edge_num_list = list()
    OF_list = list()

    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    #p1
    x_1 = N_1a + N_1b + N_2a + N_2b +  N_2c + N_3 -\
                          (N_1a*N_1a + N_1b*N_1a + N_2a*N_1a + N_2b*N_1a +  N_2c*N_1a + N_3*N_1a +
                           N_1b*N_1b + N_2a*N_1b + N_2b*N_1b +  N_2c*N_1b + N_3*N_1b +
                            N_2a*N_2a + N_2b*N_2a +  N_2c*N_2a + N_3*N_2a +
                           N_2b*N_2b +  N_2c*N_2b + N_3*N_2b +
                            N_2c*N_2c + N_3*N_2c +
                           N_3*N_3
                           )/m
    edge_num_list.append(x_1)
    OF_list.append(0)
    #p2
    #x_2 = x_1 + 3*N_3line - 6*N_3 - 5 * N_2a - 4 * N_1a
    #edge_num_list.append(x_2)
    #OF_list.append(OF3(n, p) - dis2_relations(n,p))
    #p3
    #x_3 = x_2 + 2*N_2line - 4* N_1b - 4* N_2b - 4*N_2c
    #edge_num_list.append(x_3)
    #OF_list.append(OF3(n, p) - (m - N_3line/12 - N_2line/3))
    #p4
    edge_num_list.append(m)
    OF_list.append(OF5(n, p))

    return edge_num_list, OF_list






if __name__ == "__main__":
    main()
