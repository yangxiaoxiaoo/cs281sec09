'''
since non-facebook graphs dont have a clear cut-off value,
using a hard cut-off function to decide sizes
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def cut_off_function(sum):
    #decide the cut off value of a max size of clusters
    return int(sum * 0.8)

nodenum_list = list()
largest_list = list()
blocknum_list = list()

fin = '/net/data/graph-models/louvain-clusters/blocksizes_new.txt'
fout = "/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt"
with open(fin, 'r') as blockfile:
    for line in blockfile:
        name = line.split(' ')[0]
        large_count = 0
        values = line.strip(name + ' ').strip('[').strip(']\n').split(',')
        node_num = sum(map(lambda x: int(x), values))
        max_cluster = int(values[-1])
        cut_off = cut_off_function(node_num)
        covered = 0
        for string_value in values:
            if covered <= cut_off:
                covered += int(string_value)
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