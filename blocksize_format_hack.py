'''only use once, for transforming bad format back
'''

with open('blocksizes.txt', 'r') as f:
    first_line = f.readline()
with open('new_blocksizs.txt', 'w') as fout:
    fout.write(first_line.replace(']', ']\n'))
