'''
since non-facebook graphs dont have a clear cut-off value,
using a hard cut-off function to decide sizes
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


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
            print name
            min_size_interested = line.split(' ')[2]
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

    plt.scatter(bigger_node_sizes, bigger_edge_sizes,color='red')
    plt.scatter(smaller_node_sizes, smaller_edge_sizes,color='blue')
    plt.savefig("plot_clusterdensity.pdf", facecolor='w', edgecolor='w',orientation='portrait')


if __name__ == "__main__":
    cut_cover90()

    #plot_density()