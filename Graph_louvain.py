import community
import sys
import networkx


'''
new usage:
python Graph_louvain.py "/net/data/graph-models/realgraph/Chicago_2008.ncol"
'''




def convert(inputf, outputf):
    #convert input an lgl to output an edgelist file
    with open(outputf, "w") as fout:
        with open(inputf, "r")as fin:
            s = 0
            t = 0
            for line in fin:
                if line[0] == '#':
                    s = int(line.split(' ')[1])
                else:
                    t = int(line)
                    if not (s==0 and t==0):
                        fout.write(str(s) + " " + str(t) + "\n")

def decide_block_num(G,name):
    #community best partition -  louvain method
    partition = community.best_partition(G)
    sizes = list()
    for comm in set(partition.values()):
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == comm]
        size_com = len(list_nodes)
        sizes.append(size_com)

    sizes.sort()
    print sizes
    with open("blocksizes.txt", 'a') as fout:
        fout.write(str(name)+ ' ' + str(sizes)+'\n')


def partition(graphname):
    '''
    old,
usage: python Graph_louvain.py /home/cbw/sbm/fb/Egypy_2008.lgl
will append result into output file "blocksizes.txt"
'''
    shortname = graphname.split('/')[-1].strip('.lgl')
    convert(graphname, "/home/xiaofeng/facebook/sparsify/cs281sec09/" + shortname + ".ncol")
    decide_block_num(networkx.read_edgelist(shortname + ".ncol"), shortname)

def main(graph):
    '''
    new,
will append result into output file "blocksizes_new.txt"
and record for each graph a file in "nnum-enum-nlist" with
cluster index, cluster node numbers, cluster edge numbers, who is in cluster.
'''
    shortname = str(graph.split('/')[-1].strip('.ncol'))
    nxgraph = networkx.read_edgelist(graph)
    partition = community.best_partition(networkx.read_edgelist(graph))
    sizes = list()
    count = 0
    for com in set(partition.values()):
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
        size_com = len(list_nodes)
        sizes.append(size_com)
        numedges = networkx.number_of_edges(nxgraph.subgraph(list_nodes))
        with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + shortname +".density", 'a') as fout1:
            fout1.write(str(count) +' ' + str(size_com) + ' ' + str(numedges) + str(list_nodes) + '\n')
    sizes.sort()
    with open("/net/data/graph-models/louvain-clusters/blocksizes_new.txt", 'a') as fout:
        fout.write( shortname + ' ' + str(sizes)+'\n')


if __name__ == "__main__":
    #partition(sys.argv[1])

    main(sys.argv[1])