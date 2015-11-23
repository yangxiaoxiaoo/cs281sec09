'''community not installed on other clusters!
'''

import os
import subprocess

path = "/home/cbw/sbm/fb/"
files = os.listdir(path)

processed = set()
queue_this_time = list()
with open("blocksizes.txt", 'r')as frefer:
    for line in frefer:
        processed.add(line.split(' ')[0])
for f in files:
    if f.strip('.lgl') not in processed:
        queue_this_time.append(f)

for i in range(0, len(queue_this_time)):
    graphfile = os.path.join(path, queue_this_time[i])
    subprocess.check_call(['python',
         '/home/xiaofeng/facebook/sparsify/cs281sec09/Graph_louvain.py',
         graphfile])
