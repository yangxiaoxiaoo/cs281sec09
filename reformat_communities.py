#reformat communities edges

import os

def reform_communities():
    filepath = "/net/data/graph-models/louvain-clusters/communities/"
    for file in os.listdir(filepath):
        fin = open(os.path.join(filepath, file),"r")
        fout = open(os.path.join(filepath, file + ".new"), "w")
        for line in fin:
            fout.write(line.replace("{}", "1"))
        fin.close()
        fout.close()

def reform_motifs():
    check_dup_set = set()
    infile =open('/net/data/graph-models/sim-graphs/approx5-json-inter', 'r')
    outfile =open('/net/data/graph-models/sim-graphs/approx5-json', 'a')
    for line in infile:
        if line not in check_dup_set:
            check_dup_set.add(line)
            outfile.write(line)
    infile.close()
    outfile.close()


def reform_json():
    fin = open('approx5-json', 'r')
    fout = open('approx5-json-2', 'w')
    for line in fin:
        line_new =  line[7:]
        fout.write(line_new)
    fin.close()
    fout.close()

if __name__ == "__main__":
    #reform_motifs()
    reform_json()