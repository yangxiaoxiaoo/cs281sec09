'''
from louvain cluster result, directly decide block p for each large(90% coverage) blocks
write result into /net/data/graph-models/louvain-clusters/block_paras
and plot p to size of blocks for these large blocks
'''



def main():

    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        bigger_node_sizes = list()
        p_values = list()
        for line in fin:
            name = line.split(' ')[0]
            print name
            min_size_interested = int(line.split(' ')[2])
            with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                for line in fin2:
                    node_num = int(line.split(' ')[1])
                    edge_num = int(line.split(' ')[2].split('[')[0])
                    if node_num > min_size_interested:
                        complete_num = node_num * (node_num - 1) / 2
                        p = edge_num / complete_num
                        print p
                        bigger_node_sizes.append(node_num)
                        p_values.append(p)

if __name__ == "__main__":
    main()