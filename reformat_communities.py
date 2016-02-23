#reformat communities edges

import os

if __name__ == "__main__":
    filepath = "/net/data/graph-models/louvain-clusters/communities/"
    for file in os.listdir(filepath):
        fin = open(os.path.join(filepath, file),"r")
        fout = open(os.path.join(filepath, file + ".new"), "w")
        for line in fin:
            fout.write(line.replace("{}", "1"))
        fin.close()
        fout.close()
