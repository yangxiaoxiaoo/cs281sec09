import os
import subprocess

'''
FIXME: community not installed on other clusters!


distribute into multiple achtung threads
for all facebook graphs, do louvain clustering, white cluster size into an output file "blocksizes.txt"

afterwards, plot that file and decide number of blocks for SBM fitting (3 iterations)
'''

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

machines = ["achtung%02i" % (x) for x in range(2, 12)]

procs = []
for i, machine in enumerate(machines):
  cmd = ['ssh',
         machine,
         'python',
         '/home/xiaofeng/facebook/sparsify/cs281sec09/Graph_louvain.py',
         os.path.join(path, queue_this_time[i])
         ]

  procs.append(subprocess.Popen(cmd))


for proc in procs:
  proc.wait()

