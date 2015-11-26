'''community not installed on other clusters!
'''

import os
import subprocess

path = "/home/cbw/sbm/"
#files = os.listdir(path)
file_list = list()
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        file_list.append(os.path.join(root, name))


processed = set()
queue_this_time = list()
with open("blocksizes.txt", 'r')as frefer:
    for line in frefer:
        processed.add(line.split(' ')[0])
for f in file_list:
    if f.strip('.lgl') not in processed:
        if len(f.split('.')) == 2 and f.split('.')[1] == 'lgl':
            queue_this_time.append(f)

for i in range(0, len(queue_this_time)):
    graphfile = os.path.join(path, queue_this_time[i])
    subprocess.check_call(['python',
         '/home/xiaofeng/facebook/sparsify/cs281sec09/Graph_louvain.py',
         graphfile])
