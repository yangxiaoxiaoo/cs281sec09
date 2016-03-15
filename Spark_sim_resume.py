#!/usr/bin/python
import subprocess
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import json
import pickle
from networkx.readwrite import json_graph
import networkx as nx
import itertools



def main():

    sc = SparkContext(appName="Motif_counting")
    collapsed_patterns = sc.textFile("hdfs://scrapper/user/xiaofeng/patterns_queue1")
    output_file_inter = "/net/data/graph-models/sim-graphs/approx5-json-inter"
    non_iso_set = set()

    def iso_json(string1,string2):
        dataG1 = json.loads(string1)
        graph1 = json_graph.node_link_graph(dataG1)
        dataG2 = json.loads(string2)
        graph2 = json_graph.node_link_graph(dataG2)
       # return nx.is_isomorphic(graph1, graph2)
        return nx.faster_could_be_isomorphic(graph1, graph2)

    flip = True
    while True:
        if flip:
            left_size = collapsed_patterns.count()
            print "left RDD size to be processed:"
            print left_size
            if left_size <= 1:
                return 0
            povet = collapsed_patterns.take(1)[0]#BROADCAST
            povet_broad = sc.broadcast(povet)
            non_iso_set.add(povet)
            fout_inter = open(output_file_inter, 'a')
            fout_inter.write(str(left_size) + ' ' + povet + '\n')
            fout_inter.close()
            collapsed_patterns_new = collapsed_patterns.filter(lambda x: not iso_json(x, povet_broad.value))
            collapsed_patterns.unpersist()
            flip = not flip
        else:
            left_size = collapsed_patterns_new.count()
            print "left RDD size to be processed:"
            print left_size
            if left_size <= 1:
                return 0
            povet = collapsed_patterns_new.take(1)[0]#BROADCAST
            povet_broad = sc.broadcast(povet)
            non_iso_set.add(povet)
            fout_inter = open(output_file_inter, 'a')
            fout_inter.write(str(left_size) + ' ' + povet + '\n')
            fout_inter.close()
            collapsed_patterns = collapsed_patterns_new.filter(lambda x: not iso_json(x, povet_broad.value))
            collapsed_patterns_new.unpersist()
            flip = not flip


if __name__ == "__main__":
    main()
