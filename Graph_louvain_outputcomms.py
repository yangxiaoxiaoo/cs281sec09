import community
import sys
import networkx
import os
import subprocess


def write_communities(graph, name_to_size):

    shortname = str(graph.split('/')[-1].strip('.ncol'))
    nxgraph = networkx.read_edgelist(graph)
    partition = community.best_partition(networkx.read_edgelist(graph))
    count = 0
    if shortname in name_to_size.keys():
        for com in set(partition.values()):
            count = count + 1.
            list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
            size_com = len(list_nodes)
            if size_com > name_to_size[shortname]:
                community_subgraph = nxgraph.subgraph(list_nodes)
                with open("/net/data/graph-models/louvain-clusters/communities/" + shortname +"_" +str(count), 'a') as fout1:
                    networkx.write_edgelist(community_subgraph, fout1)


def threshold():
    name_to_size = dict()
    deletedset = set(['roadNet-CA', 'roadNet-PA','roadNet-TX', 'web-BerkSta', 'web-Google', 'web-NotreDame','web-Stanford'])
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            min_size_interested = int(line.split(' ')[2])
            if name not in deletedset:
                name_to_size[name] = min_size_interested
    return name_to_size


def main():
    name_to_size = threshold()
    path = "/net/data/graph-models/realgraph"
    for file in os.listdir(path):
        write_communities(os.path.join(path,file), name_to_size)


if __name__ == "__main__":
    main()
