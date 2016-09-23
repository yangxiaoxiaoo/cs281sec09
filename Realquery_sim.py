from graph_models import *
import networkx
import time
import random
import motif_expectations

def querytime(Graphname):
    G = networkx.read_edgelist("/net/data/graph-models/realgraph/" + Graphname + ".ncol")
    nodelist = G.nodes()
    seednode = random.choice(nodelist)
    print Graphname + " query "+str(seednode) +"is: "
    ts1 = time.time()
    print len(motif_expectations.hop3(G, seednode))
    ts2 = time.time()
    t_interval = ts2 - ts1
    print "Time it takes is " + str(t_interval)
    return  t_interval

def creatlist():
    fin = open("blocknumbers_auto200.txt", 'r')
    Graphnames = list()
    for line in fin:
        Graphname = line.split(' ')[0]
        Graphnames.append(Graphname)
    return Graphnames


def main():
    graphlist = creatlist()
    for graphname in graphlist:
        time = querytime(graphname)
        fout = open("Realquery_time.txt", "a")
        fout.write(graphname + ", time is: " + str(time) + "\n")
        fout.close()

if __name__ == "__main__":
    main()

