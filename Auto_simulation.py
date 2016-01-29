import Simulation_generated_graph
import os
import matplotlib.pyplot as plt
import networkx as nx
import itertools

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
        if any(nx.is_isomorphic(item, item2) for item2 in deisoed_set):
            pass
        else:
            deisoed_set.add(item)
    return deisoed_set

def merge_nodes(G,node1,node2):
    for neighbor in G.neighbors(node1):
        G.add_edge(neighbor, node2)
    G.remove_node(node1)
    return G

def patternsets2(MotifG1, MotifG2):
    #enumerate all possible permutations of node labels,
    #minimum is sharing one edge, all the way to max is the smaller number of edges, complexity 2^edgenum_max
    #return a set

    patternset = set()
    edgenum_max = min(MotifG1.number_of_edges(), MotifG2.number_of_edges())

    #one edge overlap case
    for edge in MotifG1.edges():
        s = edge[0]
        t = edge[1]
        for edge2 in MotifG2.edges():
            #union requires the two Graph has no common nodes
            new_collapse = nx.union(MotifG1, MotifG2)


    #select L (two+) edges to overlap
    for L in range(0, edgenum_max + 1):
        mapping1 = dict()
        mapping2 = dict()
        for subset1 in itertools.combinations(MotifG1.edges(),L):
            for subset2 in itertools.combinations(MotifG2.edges(),L):
                permutation1 = list(itertools.permutations(subset1)).pop()
                permutation2 = list(itertools.permutations(subset2)).pop()
                for edge1 in permutation1:
                    for edge2 in permutation2:






def enumerateall():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3, color='r')
    G_1a.add_edge(3, 4)
    G_1a.add_edge(4, 1)

    G_1b = nx.Graph()
    G_1b.add_edge(5, 6)
    G_1b.add_edge(6, 7)
    G_1b.add_edge(5, 7, color='r')
    #make sure theat all nodes have different names at this moment

    allpatterns = set()
    Motifset = set([G_1a, G_1b])
    for Motif1 in Motifset:
        for Motif2 in Motifset:
            allpatterns = allpatterns.union(patternsets2(Motif1, Motif2))

    return deisomorphism(allpatterns)

def test():
    G_1a = nx.Graph()
    G_1a.add_edge(1, 2)
    G_1a.add_edge(2, 3)
    print (len(merge_nodes(G_1a,1, 3)) == 2)

if __name__ == '__main__':

    #enumerateall()
    test()
