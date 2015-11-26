import community
import sys
import networkx



'''
usage: python Graph_louvain.py /home/cbw/sbm/fb/Egypy_2008.lgl
will append result into output file "blocksizes.txt"
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
    shortname = graphname.split('/')[-1].strip('.lgl')
    convert(graphname, "/home/xiaofeng/facebook/sparsify/cs281sec09/" + shortname + ".ncol")
    decide_block_num(networkx.read_edgelist(shortname + ".ncol"), shortname)


if __name__ == "__main__":
    partition(sys.argv[1])
 #   main()