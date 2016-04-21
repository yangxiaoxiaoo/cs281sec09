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
    deletedset = set(['roadNet-CA', 'roadNet-PA','roadNet-TX', 'web-BerkSta', 'web-Google', 'web-NotreDame','web-Stanford', 'email-EuA','soc-sign-epinions'])
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            blocknum = int(line.split(' ')[1])
            if name not in deletedset:
                blocknum_list.append(blocknum)
    pvalue_plot.pre_CDF_title(blocknum_list, 200, "CDF_90blocknums")

'''
######once used to decide road and web networks should be eliminated
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
    nodes_1 = nodes.scatter(interested_node_sizes, interested_p_values,color='red', label="fewblocks")
    nodes_2 = nodes.scatter(other_node_sizes, other_p_values, color="blue", label= 'manyblocks')
    plt.ylabel('p-value')
    plt.xscale('log')
    plt.xlabel('number of nodes')
    handles, labels = nodes.get_legend_handles_labels()
    plt.legend(handles, labels)
    plt.savefig("plot_pvalues_threshold" +str(threshold) +".pdf", facecolor='w', edgecolor='w',orientation='portrait')
    print(len(dataset_names))
    for item in dataset_names:
        print item
'''

def main():
    bigger_node_sizes = list()
    p_values = list()
    deletedset = set(['roadNet-CA', 'roadNet-PA','roadNet-TX', 'web-BerkSta', 'web-Google', 'web-NotreDame','web-Stanford', 'email-EuA','soc-sign-epinions'])
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            min_size_interested = int(line.split(' ')[2])
            if name not in deletedset:
                with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                    if True:
               #     with open("/net/data/graph-models/louvain-clusters/block_paras/" + name + ".pvalue", 'w') as fout:
                        for line in fin2:
                            node_num = int(line.split(' ')[1])
                            edge_num = int(line.split(' ')[2].split('[')[0])
                            if node_num > min_size_interested:
                                complete_num = node_num * (node_num - 1) / 2
                                p = float(edge_num) / float(complete_num)
                           #     fout.write(str(node_num) + ' ' + str(p) + '\n')
                                bigger_node_sizes.append(node_num)
                                p_values.append(p)
'''

 #   error_rate = 0.05
  #  N_list1, P_list1 = Simulation_generated_graph.decidePforN_34(error_rate, max(bigger_node_sizes))
    error_rate = 0.1
    N_list2, P_list2 = Simulation_generated_graph.decidePforN_34(error_rate, max(bigger_node_sizes))
  #  error_rate = 0.15
   # N_list3, P_list3 = Simulation_generated_graph.decidePforN_34(error_rate, max(bigger_node_sizes))

#    outfile = "gnudata/pvalue_errordots.data"
 #   with open(outfile, 'w') as outfile:
  #      for i in range(0, len(bigger_node_sizes)):
   #         outfile.write(str(bigger_node_sizes[i]) +' '+ str(p_values[i])+ '\n')

    outfile = "gnudata/pvalue_errorline_34.data"
    with open(outfile, 'w') as outfile:
        for i in range(0, len(N_list2)):
            outfile.write(str(N_list2[i]) +' '+ str(P_list2[i])+' '+ '\n')


    plotline = plt.subplot(111)
    nodes = plt.scatter(bigger_node_sizes, p_values,color='red', label="nodes")
    errorline = plt.plot(N_list1, P_list1, color="blue", label= "5% error")
    errorline2 = plt.plot(N_list2, P_list2, color="green", label= "10% error")
    errorline3 = plt.plot(N_list3, P_list3, color="purple", label= "15% error")



    plt.ylabel('p-value')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('number of nodes')
    handles, labels = plotline.get_legend_handles_labels()
    plt.legend(handles, labels)
    plt.savefig("plot_pvalue_errorline.pdf", facecolor='w', edgecolor='w',orientation='portrait')
'''


def errorline():
    error_rate = 0.1
    N_list2, P_list2 = Simulation_generated_graph.decidePforN_34(error_rate, 1000000)
    outfile = "gnudata/pvalue_errorline_34.data"
    with open(outfile, 'w') as outfile:
        for i in range(0, len(N_list2)):
            outfile.write(str(N_list2[i]) +' '+ str(P_list2[i])+' '+ '\n')



if __name__ == "__main__":
    errorline()
    #main()
    #dataset_threshold()
    #dataset_select(100)