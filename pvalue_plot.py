import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


import numpy as np
from scipy.stats import norm
from bisect import bisect_left




def pre_CDF_title(input_data, point,input_title):

    Range_low = float(min(input_data))
    Range_up = float(max(input_data))
    sorted_data = sorted(input_data)


    print 'Range_up = '
    print Range_up
    print 'Range_low = '
    print Range_low
    step_len = (Range_up - Range_low)/point
    count = [0]*point
    CDF = list()
    N = len(input_data)
    print 'N ='
    print N

    for i in range(0, N):
        for j in range(0, point):
            if input_data[i] <= Range_low + j * step_len:
                count[j] += 1

    for item in count:
        CDF.append(float(item/float(N)))


    x = list()
    x.append(Range_low)
    for count in range(1,len(CDF)):
        x.append(Range_low + float(count)*step_len)

    fp = open(input_title,'w')

    i = 0
    print x[i]
    fp.write(str(x[i]) + ' '+ str(CDF[i])+'\n')


    print "lenx and len(CDF) = "
    print len(x)
    print len(CDF)


    for i in range(1, point, 1):
        print x[i]
        fp.write(str(x[i]) + ' '+ str(CDF[i])+'\n')
    fp.write(str(Range_up)+' ' + '1'+ '\n')



def main():
    bigger_node_sizes = list()
    p_values = list()
    with open("/net/data/graph-models/louvain-clusters/blocknum_threshold_90.txt", 'r') as fin:
        for line in fin:
            name = line.split(' ')[0]
            min_size_interested = int(line.split(' ')[2])
            with open("/net/data/graph-models/louvain-clusters/nnum-enum-nlist/" + name + ".density", 'r') as fin2:
                for line in fin2:
                    node_num = int(line.split(' ')[1])
                    edge_num = int(line.split(' ')[2].split('[')[0])
                    if node_num > min_size_interested:
                        complete_num = node_num * (node_num - 1) / 2
                        p = float(edge_num) / float(complete_num)
                        bigger_node_sizes.append(node_num)
                        p_values.append(p)


    pre_CDF_title(p_values, 10000,"cdf_pvalue")



if __name__ == "__main__":
    main()