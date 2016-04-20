#Experiment with real data to find supporting statistics


import os

def IS_line_meta(line):
    if line[0].isdigit():
        return False
    else:
        return True

def get_original_count(S):
    #S = 3, 4, 5, 6
    #for each name, number of blocks, get a number of motifs, and find those sharing nodes


    subid = 0
    motifnum = 0
    counts = dict()#from name to number of motifs
    overlaplists = dict()#from name to list of overlapping nodes

    def readmeta(line):
        if line.split(' ')[0]=="subgraph":
            subid = line.split(' ')[3]
        if line.split(' ')[0]=="Partial":
            motifnum = line.split(' ')[3]


    fin_dir = "/net/data/graph-models/louvain-clusters/communities_sub"
    for file in os.listdir(fin_dir):
        with open(file, 'r') as mfinder:
            name = file.split('_')[0]
            blocknum = file.split('.')[0].split('_')[1]
            Motifset = set()
            for line in mfinder:
                if not IS_line_meta(line):
                    motif_nodelist = line.strip('\n').split('\t')
                    Motifset.add(motif_nodelist)
                else:
                    readmeta(line)

    return counts, overlaplists


def get_2_motifs(overlaplists):



def main():
    for S in range(3, 7):
        counts, overlaplists = get_original_count(S)
