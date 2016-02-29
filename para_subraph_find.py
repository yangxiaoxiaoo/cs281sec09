#process clusteres in parallel, output subgraph membership for later checkings
import networkx as nx
import os
import subprocess
import numpy as np

def Motifsets():
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

    return set([G_1a, G_1b, G_2a, G_2c, G_3])





def get_graph_ids(size):
    list_of_ids = list()
    all_motifs = Motifsets()
    for graph in all_motifs:
        if graph.number_of_nodes() == size:
            A = np.array(nx.adjacency_matrix(graph))
            print A
            value = 0
            for i in range(0, size):
                for j in range(0, size ):
                    if A[i][j]:
                        value += pow(2, (i* size + j))
            print value
            list_of_ids.append(value)

    return list_of_ids

def test():
    for i in range(1, 7):
        print get_graph_ids(i)


def main():

    machines = ["achtung%02i" % (x) for x in range(2, 12)]

    m_size = 2
    while m_size <= 6:
        graph_ids = get_graph_ids(m_size)
        print "graph ids"
        print graph_ids

        filepath = "/net/data/graph-models/louvain-clusters/communities/"
        filenames = list()
        for file in os.listdir(filepath):
            if file.split('.')[-1]== 'new':
                filename = os.path.join(filepath, file)
                filenames.append(filename)


        while len(filenames) > 0:
            procs = []
            for i, machine in enumerate(machines):
                if len(filenames) > 0:
                    filename = filenames.pop()
                    if len(graph_ids) == 1: #other sizes motif
                        cmd = ['ssh',
                        machine,
                        "facebook/sparsify/mfinder1.21/mfinder",
                        filename,
                        "-s",
                        str(m_size),
                        "-f",
                        "/net/data/graph-models/louvain-clusters/communities_sub/"+filename.split("/")[-1] +"_s"+str(m_size),
                        "-r",
                        "2",
                        "-ospmem",
                        str(graph_ids[0]),
                        "-nd",
                        "-omem"
                        ]
                        print cmd
                        procs.append(subprocess.Popen(cmd))

                    if len(graph_ids) == 2: #size 4 motif: multiple possible shapes
                        cmd = ['ssh',
                        machine,
                        "facebook/sparsify/mfinder1.21/mfinder",
                        filename,
                        "-s",
                        str(m_size),
                        "-f",
                        "/net/data/graph-models/louvain-clusters/communities_sub/"+filename.split("/")[-1]+"_s"+str(m_size),
                        "-r",
                        "2",
                        "-omem",
                        "-nd"
                        ]
                        print cmd

                        procs.append(subprocess.Popen(cmd))

            for proc in procs:
                proc.wait()

        m_size += 1


if __name__ == "__main__":
    #test()
    main()
