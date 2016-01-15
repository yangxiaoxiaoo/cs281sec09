'''
from louvain cluster result, directly decide block p for each large(90% coverage) blocks
write result into /net/data/graph-models/louvain-clusters/block_paras
and plot p to size of blocks for these large blocks
----
Jan15: added line of 3-approximations
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import Simulation_generated_graph

def main():
    bigger_node_sizes = list()
    p_values = list()
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            min_size_interested = int(line.split(' ')[2])
            with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                with open("/net/data/graph-models/louvain-clusters/block_paras/" + name + ".pvalue", 'w') as fout:
                    for line in fin2:
                        node_num = int(line.split(' ')[1])
                        edge_num = int(line.split(' ')[2].split('[')[0])
                        if node_num > min_size_interested:
                            complete_num = node_num * (node_num - 1) / 2
                            p = float(edge_num) / float(complete_num)
                            fout.write(str(node_num) + ' ' + str(p) + '\n')
                            bigger_node_sizes.append(node_num)
                            p_values.append(p)

                            if p == 1.0:
                                print name
                                print node_num

    N_list, P_list = Simulation_generated_graph.decidePforN(0.5,max(bigger_node_sizes))

    nodes = plt.scatter(bigger_node_sizes, p_values,color='red')
    errorline = plt.plot(N_list, P_list, color="blue")
    plt.ylabel('p-value')
    plt.xscale('log')
    plt.xlabel('number of nodes')
    plt.legend([(nodes, errorline)], ["90%nodes","0.5errorline"])
    plt.savefig("plot_pvalue_errorline.pdf", facecolor='w', edgecolor='w',orientation='portrait')


if __name__ == "__main__":
    main()