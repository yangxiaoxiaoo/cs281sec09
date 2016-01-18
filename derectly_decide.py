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
import pvalue_plot

def dataset_threshold():
    blocknum_list = list()
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            blocknum = int(line.split(' ')[1])
            blocknum_list.append(blocknum)
    pvalue_plot.pre_CDF_title(blocknum_list, 200, "CDF_90blocknums")


def dataset_select(threshold):
    dataset_names = set()
    interested_node_sizes = list()
    interested_p_values = list()
    other_node_sizes = list()
    other_p_values = list()
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            min_size_interested = int(line.split(' ')[2])
            blocknum = int(line.split(' ')[1])
            with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                for line in fin2:
                    node_num = int(line.split(' ')[1])
                    edge_num = int(line.split(' ')[2].split('[')[0])
                    if node_num > min_size_interested:
                        complete_num = node_num * (node_num - 1) / 2
                        p = float(edge_num) / float(complete_num)
                        if blocknum > threshold:
                            #too much blocks to cover 90% nodes
                            dataset_names.add(name)
                            other_node_sizes.append(node_num)
                            other_p_values.append(p)
                        else:
                            #reasonable number of blocks to cover
                            interested_node_sizes.append(node_num)
                            interested_p_values.append(p)

    nodes = plt.subplot(111)
    nodes_1 = nodes.scatter(interested_node_sizes, interested_p_values,color='red')
    nodes_2 = nodes.scatter(other_node_sizes, other_p_values, color='blue')
    plt.ylabel('p-value')
    plt.xscale('log')
    plt.xlabel('number of nodes')
    handles, labels = nodes.get_legend_handles_labels()
    plt.legend(handles, labels)
    plt.savefig("plot_pvalues_threshold" +str(threshold) +".pdf", facecolor='w', edgecolor='w',orientation='portrait')



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

    N_list, P_list = Simulation_generated_graph.decidePforN(5,max(bigger_node_sizes))

    nodes, = plt.scatter(bigger_node_sizes, p_values,color='red')
    errorline, = plt.plot(N_list, P_list, color="blue")
    plt.ylabel('p-value')
    plt.xscale('log')
    plt.xlabel('number of nodes')
    plt.savefig("plot_pvalue_errorline.pdf", facecolor='w', edgecolor='w',orientation='portrait')


if __name__ == "__main__":
    #main()
    #dataset_threshold()
    dataset_select(100)