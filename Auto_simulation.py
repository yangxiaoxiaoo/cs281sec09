import Simulation_generated_graph
import os
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import json
from networkx.readwrite import json_graph


FIG_FOLDER = "./figs/"


def draw_motif(M, fname):
    G, pos = M.G, M.pos
    plt.clf()
    plt.figure(figsize=M.dims)

    for u, v in G.edges():
        if 'color' not in G[u][v]:
            G[u][v]['color'] = 'black'
    colors = [G[u][v]['color'] for u, v in G.edges()]

    if not hasattr(M, 'node_size'):
        M.node_size = 5000

    if len(M.labels) == 0:
        for i, u in enumerate(sorted(G.nodes())):
            M.labels[u] = chr(ord('a') + i)
    nx.draw(G, pos=pos, labels=M.labels, linewidths=2, node_size=M.node_size,
            node_color='w', width=4, edge_color=colors, font_size=M.n_font_size,
            )
    if len(M.edge_labels) == 0:
        i = 1
        for u, v in sorted(G.edges()):
            M.edge_labels[(u, v,)] = i
            i = i + 1
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=M.edge_labels,
                                 font_size=M.e_font_size)
    plt.savefig(FIG_FOLDER + fname)
    # plt.show()
    return


class Motif():
    def __init__(self, G, pos, dims):
        self.G = G
        self.pos = pos
        self.dims = dims
        self.labels = {}
        self.edge_labels = {}
        self.e_font_size = 36
        self.n_font_size = 36



def motif_A():#1a
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(2, 3, color='r')
    G.add_edge(3, 4)
    G.add_edge(4, 1)
    pos = {}
    pos[1] = (-1, 1)
    pos[2] = (1, 1)
    pos[3] = (1, -1)
    pos[4] = (-1, -1)
    M = Motif(G, pos, (8, 8))
    return M


def motif_B():
    G = nx.Graph()
    G.add_edge(1, 2, color='r')
    G.add_edge(2, 3)
    G.add_edge(1, 3)
    G.add_edge(3, 4)
    pos = {}
    pos[1] = (0, 0)
    pos[2] = (-0.1, 0.5)
    pos[3] = (0, 1)
    pos[4] = (0, 2)
    M = Motif(G, pos, (4, 8))
    return M


def motif_C():
    G = nx.cycle_graph(5)
    pos = {}
    pos[0] = (0, 0)
    pos[1] = (1, 0)
    pos[2] = (1.3, 0.8)
    pos[3] = (0.5, 1.3)
    pos[4] = (-0.3, 0.8)
    M = Motif(G, pos, (8, 8))

    return M


def motif_D():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(2, 3, color='r')
    G.add_edge(3, 4)
    G.add_edge(4, 1)
    G.add_edge(1, 5)
    pos = {}
    pos[1] = (-1, 0)
    pos[2] = (0, 0)
    pos[3] = (1, 0)
    pos[4] = (0, -1)
    pos[5] = (-2, 0)
    label = {}
    label[1] = 'c'
    label[2] = 'b'
    label[3] = 'a'
    label[4] = 'e'
    label[5] = 'd'
    M = Motif(G, pos, (8, 4))
    M.labels = label
    return M


def motif_E():
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(1, 3, color='r')
    pos = {}
    pos[1] = (0, 0)
    pos[2] = (-0.1, 0.5)
    pos[3] = (0, 1)
    M = Motif(G, pos, (4, 4))
    return M


def motif_F():
    # the annoying one...
    G = nx.cycle_graph(6)
    pos = {}
    pos[0] = (0, 0)
    pos[1] = (1, 1)
    pos[2] = (1, 2)
    pos[3] = (0, 3)
    pos[4] = (-1, 2)
    pos[5] = (-1, 1)

    # outer edge
    G.add_edge(6, 7)
    G.add_edge(7, 8)
    G.add_edge(8, 9, color='r')
    pos[6] = (1.5, 2)
    pos[7] = (1.5, 1)
    pos[8] = (0, -.5)
    pos[9] = (-1.5, 1)

    labels = {}
    labels[0] = 'a'
    labels[1] = 'b'
    labels[2] = 'c'
    labels[3] = 'd'
    labels[4] = 'e'
    labels[5] = 'f'

    labels[6] = 'c'
    labels[7] = 'b'
    labels[8] = 'a'
    labels[9] = 'f'

    M = Motif(G, pos, (8, 8))
    M.labels = labels
    M.node_size = 1000
    M.n_font_size = 18
    return M


def motif_G():
    G = nx.Graph()
    G.add_edge('a', 'b')
    G.add_edge('b', 'c')
    G.add_edge('c', 'd', color='r')

    pos = {}
    pos['a'] = (0, 0)
    pos['b'] = (1, 0)
    pos['c'] = (2, 0)
    pos['d'] = (3, 0)
    M = Motif(G, pos, (8, 1))
    M.node_size = 1000
    M.e_font_size = 18
    M.n_font_size = 18
    return M


def motif_H():
    G = nx.Graph()
    G.add_edge('a', 'b')
    G.add_edge('b', 'c', color='r')

    pos = {}
    pos['a'] = (0, 0)
    pos['b'] = (1, 0)
    pos['c'] = (2, 0)
    M = Motif(G, pos, (8, 1))
    M.node_size = 1000
    M.e_font_size = 18
    M.n_font_size = 18
    return M

def deisomorphism(patternset):
    deisoed_set = set()
    for item in patternset:
        Unique = True
        for item2 in deisoed_set:
            if nx.is_isomorphic(item, item2):
                Unique = False
        if Unique:
            deisoed_set.add(item)
    return deisoed_set

def merge_nodes(G,node1,node2):
    if node1 in G and node2 in G:
        for neighbor in G.neighbors(node1):
            G.add_edge(neighbor, node2)
        G.remove_node(node1)
    return G

def patternsets2(MotifG1, MotifG2):
    #enumerate all possible permutations of node labels,
    #minimum is sharing one edge, all the way to max is the smaller number of edges, complexity 2^edgenum_max
    #return a set of possibly isomorphic collapses

    patternset = set()
    edgenum_max = min(MotifG1.number_of_edges(), MotifG2.number_of_edges())

    #select L (two+) edges to overlap
    for L in range(1, edgenum_max + 1):
        print L
        L_subsets = list(itertools.combinations(MotifG1.edges(),L))
        L_subsets2 = list(itertools.combinations(MotifG2.edges(),L))
     #   print "all possible combination of choosing"+str(L) +"edges"
     #   print L_subsets2
        for subset1 in L_subsets:
            for subset2 in L_subsets2:
                print "already chose these" +str(L)+" edges in Motif2"
                print subset2
                permutations = list(itertools.permutations(subset1))
             #   print "already chose another"+str(L)+"in Motif1, now ordering them"
             #   print permutations
                i = 0
                for permutation in permutations:
                    print "this permutation is"
                    print permutation
                    print "in this particular order" + str(i)
                    if MotifG1 == MotifG2:
                        print "waring!!!same motif non-relabled"
                        G = nx.disjoint_union(MotifG1, MotifG2)
                    else:
                        G = nx.union(MotifG1, MotifG2)

                    if len(G) != 0:
                        G2 = nx.Graph()
                        G22 = nx.Graph()
                        Motif2merged_nodes = set()
                        for j in range(0, len(permutation)):
                            edge_1 = permutation[j]
                            edge_2 = subset2[j]
                            print "edge 1"
                            print edge_1
                            print "edge 2"
                            print edge_2

                            if edge_2[0] not in Motif2merged_nodes:
                                G1 = merge_nodes(G, edge_1[0], edge_2[0])
                                Motif2merged_nodes.add(edge_2[0])
                            if edge_2[1] not in Motif2merged_nodes:
                                G2 = merge_nodes(G1, edge_1[1], edge_2[1])
                                Motif2merged_nodes.add(edge_2[1])

                            if edge_2[0] not in Motif2merged_nodes:
                                G11 = merge_nodes(G, edge_1[1], edge_2[0])
                            if edge_2[1] not in Motif2merged_nodes:
                                G22 = merge_nodes(G11, edge_1[0], edge_2[1])

                        patternset.add(G2)
                        patternset.add(G22)
                        print G2.nodes()
                    i += 1


    return patternset

def three_hop(Graph):
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

    relations = 0
    for node in Graph.nodes():
        relations += len(hop3(Graph, node))
    return relations/2


def count_loss(Motif_pattern):
    loss = 0
    for edge in Motif_pattern.edges():
        before = three_hop(Motif_pattern)
        Motif_pattern.remove_edge(*edge)
        loss = before - three_hop(Motif_pattern)
        Motif_pattern.add_edge(*edge)
    return loss

def count_appearance(Motif_pattern, N, p):
    nodes_num = Motif_pattern.number_of_nodes()
    #...unfinished

def enumerate2():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7)

    G_2a  =nx.Graph()
    G_2a.add_edge(8, 9)
    G_2a.add_edge(9, 10)
    G_2a.add_edge(10, 11)
    G_2a.add_edge(11, 12)
    G_2a.add_edge(12, 8)

  #  G_2b = nx.Graph()
  #  G_2b.add_edge(1, 2)
  #  G_2b.add_edge(2, 3)
  #  G_2b.add_edge(3, 4)
  #  G_2b.add_edge(4, 1)


    G_2c = nx.Graph()
    G_2c.add_edge(13, 14)
    G_2c.add_edge(14, 15)
    G_2c.add_edge(13, 15)
    G_2c.add_edge(15, 16)

    G_3 = nx.Graph()
    G_3.add_edge(17, 18)
    G_3.add_edge(18, 19)
    G_3.add_edge(19, 20)
    G_3.add_edge(20, 21)
    G_3.add_edge(21, 22)
    G_3.add_edge(22, 17)

    #make sure theat all nodes have different names at this moment

    allpatterns = set()
    #Motifset = set([G_1a, G_1b, G_2a, G_2c, G_3])
    Motifset = set([G_1a, G_1b])
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            if not Motif1 == Motif2:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(Motif2.nodes())
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns.add(item)
    print len(allpatterns)
    return deisomorphism(allpatterns)

def enumerate3():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7)

    G_2a  =nx.Graph()
    G_2a.add_edge(8, 9)
    G_2a.add_edge(9, 10)
    G_2a.add_edge(10, 11)
    G_2a.add_edge(11, 12)
    G_2a.add_edge(12, 8)

  #  G_2b = nx.Graph()
  #  G_2b.add_edge(1, 2)
  #  G_2b.add_edge(2, 3)
  #  G_2b.add_edge(3, 4)
  #  G_2b.add_edge(4, 1)


    G_2c = nx.Graph()
    G_2c.add_edge(13, 14)
    G_2c.add_edge(14, 15)
    G_2c.add_edge(13, 15)
    G_2c.add_edge(15, 16)

    G_3 = nx.Graph()
    G_3.add_edge(17, 18)
    G_3.add_edge(18, 19)
    G_3.add_edge(19, 20)
    G_3.add_edge(20, 21)
    G_3.add_edge(21, 22)
    G_3.add_edge(22, 17)

    #make sure theat all nodes have different names at this moment

    allpatterns = set()
    Motifset = set([G_1a, G_1b, G_2a, G_2c, G_3])
    #Motifset = set([G_1a, G_1b])
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            if len(set(Motif1.nodes()).intersection(Motif2.nodes())) == 0:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(max(Motif2.nodes()), max(Motif1.nodes()))
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns.add(item)
    print len(allpatterns)
    patterns_2 = deisomorphism(allpatterns)
    allpatterns_5_order = set()
    for Motif1 in patterns_2:
        for Motif2 in Motifset:
            if len(set(Motif1.nodes()).intersection(Motif2.nodes())) == 0:
                for item in patternsets2(Motif1, Motif2):
                    allpatterns_5_order.add(item)
            else:
                print Motif2.nodes()
                print "--->"
                node_max = max(max(Motif2.nodes()), max(Motif1.nodes()))
                to_list = range(node_max + 1,  + node_max + Motif2.number_of_nodes() +1)
                print to_list
                Motif3 = nx.relabel_nodes(Motif2, mapping=dict(zip(Motif2.nodes(),to_list)))
                print Motif3.nodes()
                for item in patternsets2(Motif1, Motif3):
                    allpatterns_5_order.add(item)
    return deisomorphism(allpatterns_5_order)


def test():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    print (len(merge_nodes(G_1a,1, 3)) == 2)
    G_2 = nx.Graph()
    G_2.add_edge(3, 2)
    print nx.is_isomorphic(G_1a, G_2)


    G_3 = nx.Graph()
    G_3.add_edge(1,2)
    G_3.add_edge(3,2)
    print not nx.is_isomorphic(G_2, G_3)
    set_of_tested_graphs = set([G_1a, G_2, G_3])
    print len(deisomorphism(set_of_tested_graphs)) == 2
    set_of_tested_graphs2 = set([G_2, G_1a])
    print len(deisomorphism(set_of_tested_graphs2)) == 1

    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7)
    Motifset = set([G_1a, G_1b])

    allpatterns = set()
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            if not Motif1.nodes() == Motif2.nodes():
                for item in patternsets2(Motif1, Motif2):
                    allpatterns.add(item)
    print len(deisomorphism(allpatterns)) == 3 #one is empty in all three
    for item in (deisomorphism(allpatterns)):
        dataG = json_graph.node_link_data(item)
        print json.dumps(dataG)




def main():
    #patterns = enumerate2()
    patterns = enumerate3()
    print len(patterns)
    output = "noniso_5order_graphs/"
    index = 1
    for item in patterns:
        #nx.draw(item)
        #plt.show()
        nx.write_edgelist(item, output + str(index))
        index += 1


    '''
    dict_number_to_loss = dict()
    for item in patterns:
        k = count_appearance(item)
        v = count_loss(item)
        dict_number_to_loss[k] = v
    '''

#recheck the same motifs ones.


if __name__ == '__main__':
    #main()
    test()
