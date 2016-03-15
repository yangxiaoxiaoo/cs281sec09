import os
inpath = "/net/data/graph-models/sim-graphs/patterns_queue1"
outpath = "/net/data/graph-models/sim-graphs/patterns_differ"
patterns_set = set()
for file in os.listdir(inpath):
    with open(os.path.join(inpath, file), 'r') as inputfile:
        for line in inputfile:
            patterns_set.add(line)

with open(outpath, 'w') as outfile:
    for item in patterns_set:
        outfile.write(item)