'''
since non-facebook graphs dont have a clear cut-off value,
using a hard cut-off function to decide sizes
'''
import numpy as np
import matplotlib.pyplot as plt

def cut_off_function(max):
    #decide the cut off value of a max size of clusters
    return int(max/200)

nodenum_list = list()
largest_list = list()
blocknum_list = list()

fin = 'blocksizes.txt'
with open(fin, 'r') as blockfile:
    for line in blockfile:
        name = line.split(' ')[0]
        large_count = 0
        values = line.strip(name + ' ').strip('[').strip(']\n').split(',')
        max_cluster = int(values[-1])
        cut_off = cut_off_function(max_cluster)
        for string_value in values:
            if int(string_value) >= cut_off:
                large_count += 1
        node_num = sum(map(int(), values))
        nodenum_list.append(node_num)
        largest_list.append(max_cluster)
        blocknum_list.append(large_count)
        outfile = open('blocknumbers_auto200.txt', 'a')
        outfile.write(str(name) + ' ' + str(large_count)+ '\n')

plt.scatter(nodenum_list, blocknum_list,color='red')
plt.savefig("plot_nodenum_blocknum.pdf", facecolor='w', edgecolor='w',orientation='portrait')

plt.scatter(nodenum_list, largest_list,color='blue')
plt.savefig("plot_nodenum_largest.pdf", facecolor='w', edgecolor='w',orientation='portrait')