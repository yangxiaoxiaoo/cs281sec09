'''
since non-facebook graphs dont have a clear cut-off value,
using a hard cut-off function to decide sizes
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np


def cut_cover90():
    #run once on the imcomplete graphs, need to run again when all 60 are ready
    def cut_off_function(sum):
        #decide the cut off value of a max size of clusters
        return int(sum * (1 - 0.9))

    nodenum_list = list()
    largest_list = list()
    blocknum_list = list()

    fin = '/net/data/graph-models/louvain-clusters/blocksizes_new.txt'
    fout = "/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt"
    with open(fin, 'r') as blockfile:
        for line in blockfile:
            name = line.split(' ')[0]
            large_count = 1
            values = line.strip(name + ' ').strip('[').strip(']\n').split(',')
            node_num = sum(map(lambda x: int(x), values))
            max_cluster = int(values[-1])
            cut_off = cut_off_function(node_num)
            non_covered = 0
            for string_value in values:
                if non_covered < cut_off:
                    non_covered += int(string_value)
                    cut_off_size = int(string_value)
                else:
                    large_count += 1


            nodenum_list.append(node_num)
            largest_list.append(max_cluster)
            blocknum_list.append(large_count)
            outf = open(fout, 'a')
            outf.write(name + ' '+ str(large_count) +' '+ str(cut_off_size) + "\n")

        #  outfile = open('blocknumbers_auto200.txt', 'a')
        #  outfile.write(str(name) + ' ' + str(large_count)+ '\n')

    #plt.scatter(nodenum_list, blocknum_list,color='red')
    #plt.savefig("plot_nodenum_blocknum.pdf", facecolor='w', edgecolor='w',orientation='portrait')

    #plt.scatter(nodenum_list, largest_list,color='blue')
    #plt.savefig("plot_nodenum_largest.pdf", facecolor='w', edgecolor='w',orientation='portrait')

def plot_density():
    #with a known cut threshhold size, plot those obove it, and those below it,
    #size - number of edges, with different colors
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        bigger_node_sizes = list()
        bigger_edge_sizes = list()
        smaller_node_sizes = list()
        smaller_edge_sizes = list()
        for line in fin:
            name = line.split(' ')[0]
            deletedset = set(['email-EuA','soc-sign-epinions', 'roadNet-CA', 'roadNet-PA','roadNet-TX', 'web-BerkSta', 'web-Google', 'web-NotreDame','web-Stanford'])
            if name not in deletedset:
                min_size_interested = int(line.split(' ')[2])
                with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                    for line in fin2:
                        node_num = int(line.split(' ')[1])
                        edge_num = int(line.split(' ')[2].split('[')[0])
                        if node_num > min_size_interested:
                            bigger_node_sizes.append(node_num)
                            bigger_edge_sizes.append(edge_num)
                        else:
                            smaller_node_sizes.append(node_num)
                            smaller_edge_sizes.append(edge_num)

    #plot a boundary of dense/sparse region
    def simulate_boundary(node_max, edge_max):
        list_of_node_size = list()
        list_of_edge_size = list()
        for n in range(1, node_max):
            rho = 1014 * math.log(n) / 0.38
            m = 2 * rho * n
           # if m < edge_max:
            list_of_node_size.append(n)
            list_of_edge_size.append(m)
        print len(list_of_edge_size)
        print len(list_of_node_size)
        return list_of_node_size, list_of_edge_size

    def simulate_connected(node_max, edge_max):
        list_of_node_size = list()
        list_of_edge_size = list()
        for n in range(2, node_max):
            list_of_node_size.append(n)
            list_of_edge_size.append(n-1)
        return list_of_node_size, list_of_edge_size



    list_of_node_size, list_of_edge_size = simulate_boundary(max(bigger_node_sizes), max(bigger_edge_sizes))
    list_of_node_size2, list_of_edge_size2 = simulate_connected(max(bigger_node_sizes), max(bigger_edge_sizes))
    print len(list_of_edge_size)
    print len(list_of_node_size)

    outfile = "gnudata/clusterdensity1.data"
    #line1: sparse_region
    with open(outfile, 'w') as outfile:
        for i in range(0, len(np.array(list_of_node_size))):
            outfile.write(str(np.array(list_of_node_size)[i]) +' '+ str(np.array(list_of_edge_size)[i])+ '\n')

    outfile = "gnudata/clusterdensity2.data"
    #line2: bigger blocks
    with open(outfile, 'w') as outfile:
        for i in range(0, len(bigger_node_sizes)):
            outfile.write(str(bigger_node_sizes[i]) +' '+ str(bigger_edge_sizes[i])+ '\n')

    outfile = "gnudata/clusterdensity3.data"
    #line3: smaller blocks
    with open(outfile, 'w') as outfile:
        for i in range(0, len(smaller_node_sizes)):
            outfile.write(str(smaller_node_sizes[i]) +' '+ str(smaller_edge_sizes[i])+ '\n')

    outfile = "gnudata/clusterdensity4.data"
    #line4: connected line
    with open(outfile, 'w') as outfile:
        for i in range(0, len(np.array(list_of_node_size2))):
            outfile.write(str(np.array(list_of_node_size2)[i]) +' '+ str(np.array(list_of_edge_size2))+ '\n')




'''
    sparse_region = plt.plot(np.array(list_of_node_size), np.array(list_of_edge_size), color = 'green', label="sparse-dense boundary")
    bigger = plt.scatter(bigger_node_sizes, bigger_edge_sizes,color='red', label="bigger nodes")
    smaller = plt.scatter(smaller_node_sizes, smaller_edge_sizes,color='blue', label="smaller nodes")
    connected_line = plt.plot(np.array(list_of_node_size2), np.array(list_of_edge_size2), color = 'black', label='connected line')
    plt.yscale('log')
    plt.ylabel('number of edges')
    plt.xscale('log')
    plt.xlabel('number of nodes')
    plt.legend(loc=2)

    plt.savefig("plot_clusterdensity.pdf", facecolor='w', edgecolor='w',orientation='portrait')
'''

if __name__ == "__main__":
    #cut_cover90()

    plot_density()