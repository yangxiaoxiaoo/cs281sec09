import os


def main():
    already_processed = "/net/data/graph-models/louvain-clusters/communities_sub/"
    for file in os.listdir(already_processed):
            data_cluster_name = file.split('_s')[0]
            with open(os.path.join(already_processed, file),'r') as member_file :
                for line in member_file:
                    if line.split(' ')[0] == "subgraph":
                        id = int(line.split(' ')[-1])
                    if line.split(' ')[0] == 'Nreal':
                        motif_num = int(line.split(' ')[-1])

