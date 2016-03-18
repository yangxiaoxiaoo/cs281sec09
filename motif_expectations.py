#calculate an stimation occrance for all shapes in 5



import matplotlib.pyplot as plt
import numpy as np
import networkx
import json
from networkx.readwrite import json_graph
import subprocess

def hop2(G, A):
    hop2_set = set()
    for neighbor in G.neighbors(A):
        hop2_set.add(neighbor)
        for neighbor2 in G.neighbors(neighbor):
            hop2_set.add(neighbor2)
    return hop2_set

def hop3(G, A):
    hop3_set = set()
    for neighbor in G.neighbors(A):
        hop3_set.add(neighbor)
        hop3_set = hop3_set.union(hop2(G, neighbor))
    return hop3_set

def edge_to_cost(edge, G_string):
    dataG = json.loads(G_string)
    G = json_graph.node_link_graph(dataG)
    A = int(edge[0])
    B = int(edge[1])
    edge = (A, B)
    local_set = hop2(G, A).union(hop2(G, B))
    local_set.add(A)
    local_set.add(B)
    interested = G.subgraph(local_set)
    hop3_before = 0
    for node in interested.nodes():
        hop3_before += len(hop3(interested, node))
    interested.remove_edge(*edge)
    hop3_after = 0
    for node in interested.nodes():
        hop3_after += len(hop3(interested, node))
    loss = (hop3_before - hop3_after)/2
    return edge, loss

def G_string_to_safe_totalcost(G_string):
    safe_edges = 0
    total_cost = 0
    dataG = json.loads(G_string)
    G = json_graph.node_link_graph(dataG)
    for edge in G.edges():
        loss = edge_to_cost(edge, G_string)[1]
        total_cost += loss
        if loss == 0:
            safe_edges += 1
    return safe_edges, total_cost

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def exp4_3(n, p):
    #how larger motifs affect the edges that can be safely removed
    fin = open('approx3-json', 'r')
    error4_3 = 0 #how many edges can be safely removed
    OF4_3 = 0 #how many 3-hop relations are there in the larger motif

    for line in fin:
      #  line_new =  line[7:]
      #  print line_new      ????why
        data = json.loads(line)
        graph1 = json_graph.node_link_graph(data)
        num_n = graph1.number_of_nodes()
        num_e = graph1.number_of_edges()
        N_graph_exp = choose(n, num_n) * pow(p, num_e) * pow((1-p), (num_n * (num_n - 1)/2 - num_e))
        edge_multiplyer, error_multiplyer = G_string_to_safe_totalcost(line)
        error4_3 += (error_multiplyer - 1 ) * N_graph_exp
        #offset from 1 from lower estimation
        OF4_3 += (edge_multiplyer - 2) * N_graph_exp
        #offset from 2 from lower estimation

    return error4_3, OF4_3

def exp5_4(n, p):
    #how larger motifs affect the edges that can be safely removed
    fin = open('approx5-json-2', 'r')
    error5_4 = 0 #how many edges can be safely removed
    OF5_4 = 0 #how many 3-hop relations are there in the larger motif

    for line in fin:
      #  line_new =  line[7:]
      #  print line_new      ????why
        data = json.loads(line)
        graph1 = json_graph.node_link_graph(data)
        num_n = graph1.number_of_nodes()
        num_e = graph1.number_of_edges()
        N_graph_exp = choose(n, num_n) * pow(p, num_e) * pow((1-p), (num_n * (num_n - 1)/2 - num_e))
        edge_multiplyer, error_multiplyer = G_string_to_safe_totalcost(line)
        error5_4 += (error_multiplyer - 1 ) * N_graph_exp
        #offset from 1 from lower estimation
        OF5_4 += (edge_multiplyer - 2) * N_graph_exp
        #offset from 2 from lower estimation

    return error5_4, OF5_4



def OF3(n, p):
    #objective function in 5 -approximation
    m = p * n *(n-1)/2

    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    Error2_3 = (N_1a * N_1b + N_1a * N_2a + N_1a * N_2b + N_1a * N_2c + N_1a* N_3
                            + N_1b * N_2a + N_1b * N_2b + N_1b * N_2c + N_1b* N_3
                                          + N_2a * N_2b + N_2a * N_2c + N_2a* N_3
                                                        + N_2b * N_2c + N_2b* N_3
                                                                      + N_2c* N_3
                + pow(N_1a, 2) + pow(N_1b, 2) + pow(N_2a, 2) + pow(N_2b, 2) + pow(N_2c, 2) + pow(N_3, 2)
            )/m

    Appx1 = m + N_3line + N_2line
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    Appx2 = Appx1 - Error1_2
    Appx3 = Appx2 + Error2_3
    return Appx3


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

    error4_3, OF4_3 = exp4_3(n, p)
    error5_4, OF5_4 = exp5_4(n, p)

    edge_num_list.append(x_1 + error4_3 + error5_4)
    OF_list.append(0)

    edge_num_list.append(m)
    OF_list.append(OF3(n, p)+ OF4_3 + OF5_4)

    return edge_num_list, OF_list

def oracle_4(n, p):
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

    error4_3, OF4_3 = exp4_3(n, p)

    edge_num_list.append(x_1 + error4_3)
    OF_list.append(0)

    edge_num_list.append(m)
    OF_list.append(OF3(n, p)+ OF4_3)

    return edge_num_list, OF_list

