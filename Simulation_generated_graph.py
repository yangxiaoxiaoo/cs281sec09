#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import motif_expectations

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def count_edges(n, p):
    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)
    return m + 2* N_2line + 3 * N_3line + 4 * N_1a + 3*N_1b + 5*N_2a + 4*N_2b + 4*N_2c + 6*N_3

def count_3hop(n, p):
    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)
  #  N_cov = N_3*

    return m + N_2line + N_3line - N_1a - N_1b - N_2a - N_2b - N_2c - N_3 #+ N_cov

def main():
    #first simulate random removal
    n = 200
    p = 0.01
    xvalue = list()
    yvalue = list()
    edge_num_ini = p * n *(n-1)/2
    for k in range(1, int(edge_num_ini)):
        p_new = p - 2*k / float(n * (n-1))
        print p_new
        hop_3 = count_3hop(n, p_new)
        xvalue.append(k)
        yvalue.append(hop_3)

   # P_1x =
   # p_1y = edge_num_ini


    baseline = plt.plot(np.array(xvalue), np.array(yvalue), color = 'green',label = 'baseline')
    plt.show(baseline)

def plot_np():

    n = 200
    p = np.arange(0, 0.2, 0.001)

    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    plt.figure(1)

    plt.subplot(211)
    Appx1 = m + N_3line + N_2line
    plt.plot(p, Appx1)
    plt.xlabel("p")
    plt.title("1-order approxamation")
    plt.subplot(212)
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    plt.plot(p, Appx1 - Error1_2)
    plt.xlabel("p")
    plt.title("1-/2- error")


    plt.show()


def plot_2appro():
    n = 500
    p = np.arange(0.001, 0.2, 0.001)
    m = p * n *(n-1)/2

    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    Error2_3 = (N_1a * N_1b + N_1a * N_2a + N_1a * N_2b + N_1a * N_2c + N_1a* N_3
                            + N_1b * N_2a + N_1b * N_2b + N_1b * N_2c + N_1b* N_3
                                          + N_2a * N_2b + N_2a * N_2c + N_2a* N_3
                                                        + N_2b * N_2c + N_2b* N_3
                                                                      + N_2c* N_3
                + pow(N_1a, 2) + pow(N_1b, 2) + pow(N_2a, 2) + pow(N_2b, 2) + pow(N_2c, 2) + pow(N_3, 2)
     )/m

    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3

    plt.figure(1)
    '''
    ax = plt.subplot(311)
    Appx1 = m + N_3line + N_2line
    p1, = ax.plot(p, Appx1, label= "1-appr")
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    plt.xlabel("p")
    plt.title("n=" + str(n)+", 1 approxamation")

    ax = plt.subplot(312)
    Appx1 = m + N_3line + N_2line
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    Appx2 = Appx1 - Error1_2
    p1, = ax.plot(p, Appx1, label= "1-appr")
    p2, = ax.plot(p, Appx2, label= "2-appr")
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    plt.xlabel("p")
    plt.title("n=" + str(n)+", 1 and 2 approxamation")

    ax = plt.subplot(111)
    Appx1 = m + N_3line + N_2line
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    Appx2 = Appx1 - Error1_2
    Appx3 = Appx2 + Error2_3
    p1, = ax.plot(p, Appx1, label= "1-appr")
    p2, = ax.plot(p, Appx1 - Error1_2, label= "2-appr")
    p3, = ax.plot(p, Appx3, label= "3-appr")
    handles, labels = ax.get_legend_handles_labels()
    ax.set_yscale('log')
    ax.legend(handles, labels)
    plt.xlabel("p")
    plt.title("n=" + str(n)+", all 3 approxamation orders")
    '''
    err = plt.subplot(111)
    p1, = err.plot(p, Error1_2, label = "error 1- to 2-")
    p2, = err.plot(p, Error2_3, label = "error 2- to 3-")
    handles, labels = err.get_legend_handles_labels()
    err.set_yscale('log')
    err.legend(handles, labels)
    plt.xlabel("p")
    plt.title("n=" + str(n) +", errors")


    plt.show()



def decidePforN(error, Nmax):
    N_list = list()
    P_list = list()

    for n in (range(1,100, 1) + range(100,Nmax,100)):

        p = np.arange(0.001, 0.2, 0.001)
        m = p * n *(n-1)/2

        N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
        N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
        N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
        N_1b = 3 * choose(n, 3) * pow(p,3)
        N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
        N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
        N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
        N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

        Error2_3 = (N_1a * N_1b + N_1a * N_2a + N_1a * N_2b + N_1a * N_2c + N_1a* N_3
                            + N_1b * N_2a + N_1b * N_2b + N_1b * N_2c + N_1b* N_3
                                          + N_2a * N_2b + N_2a * N_2c + N_2a* N_3
                                                        + N_2b * N_2c + N_2b* N_3
                                                                      + N_2c* N_3
                + pow(N_1a, 2) + pow(N_1b, 2) + pow(N_2a, 2) + pow(N_2b, 2) + pow(N_2c, 2) + pow(N_3, 2)
            )/m

        Appx1 = m + N_3line + N_2line
        Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
        Appx2 = Appx1 - Error1_2
        Appx3 = Appx2 + Error2_3

        p_diverge = 1
        for i in range(1, len(p)):
            if Appx3[i] > float(1 + error)*Appx1[i]:
                p_diverge = p[i]
                print i
                break
        if p_diverge != 0:
            N_list.append(n)
            P_list.append(p_diverge)

    return N_list, P_list

def OF1(n, p):
    #objective function in 3-approximation
    m = p * n *(n-1)/2

    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    Appx1 = m + N_3line + N_2line -(N_1a + N_1b + N_2a + N_2b + N_2c + N_3)
    return Appx1




def OF3(n, p):
    #objective function in 3-approximation
    m = p * n *(n-1)/2

    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    Error2_3 = (N_1a * N_1b + N_1a * N_2a + N_1a * N_2b + N_1a * N_2c + N_1a* N_3
                            + N_1b * N_2a + N_1b * N_2b + N_1b * N_2c + N_1b* N_3
                                          + N_2a * N_2b + N_2a * N_2c + N_2a* N_3
                                                        + N_2b * N_2c + N_2b* N_3
                                                                      + N_2c* N_3
                + pow(N_1a, 2) + pow(N_1b, 2) + pow(N_2a, 2) + pow(N_2b, 2) + pow(N_2c, 2) + pow(N_3, 2)
            )/m

    Appx1 = m + N_3line + N_2line
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    Appx2 = Appx1 - Error1_2
    Appx3 = Appx2 + Error2_3
    return Appx3

def dis2_relations(n, p):
    #objective function in 3-approximation
    m = p * n *(n-1)/2

    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)


    Error2_3 = (N_1a * N_1b + N_1a * N_2a + N_1a * N_2b + N_1a * N_2c
                            + N_1b * N_2a + N_1b * N_2b + N_1b * N_2c
                                          + N_2a * N_2b + N_2a * N_2c
                                                        + N_2b * N_2c

                + pow(N_1a, 2) + pow(N_1b, 2) + pow(N_2a, 2) + pow(N_2b, 2) + pow(N_2c, 2)
            )/m

    Appx1 = m  + N_2line
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c
    Appx2 = Appx1 - Error1_2
    Appx3 = Appx2 + Error2_3
    return Appx3


def oracle_1(n, p):
    #plot oracle lines
    edge_num_list = list()
    OF_list = list()

    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    #p1
    edge_num_list.append( N_1a + N_1b + N_2a + N_2b +  N_2c + N_3)
    OF_list.append(0)
    #p2
    #edge_num_list.append(N_1a + N_1b + N_2a + N_2b +  N_2c + N_3 + N_3line - float(1)/12 * (N_3line * N_3line/m) - 6*N_3 - 5 * N_2a - 4 * N_1a)
    #OF_list.append(OF1(n, p) - dis2_relations(n,p))
    #p3
    #edge_num_list.append(N_1a + N_1b + N_2a + N_2b +  N_2c + N_3 + N_3line - 6*N_3 - 5 * N_2a - 4 * N_1a + N_2line - 4* N_1b - 4* N_2b - 4*N_2c)
    #OF_list.append(OF3(n, p) - (m - N_3line/12 - N_2line/3))
    #p4
    edge_num_list.append(m)
    OF_list.append(OF1(n, p))

    return edge_num_list, OF_list


def oracle_3(n, p):
    #plot oracle lines
    edge_num_list = list()
    OF_list = list()

    m = p * n *(n-1)/2
    N_3line = 12 * choose(n, 4) * pow(p,3) * pow((1-p),3)
    N_2line = 3 * choose(n, 3) * pow(p,2) * (1-p)
    N_1a = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_1b = 3 * choose(n, 3) * pow(p,3)
    N_2a = 60 * choose(n, 5) * pow(p,5) * pow((1-p),5)
    N_2b = 12 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_2c = 24 * choose(n, 4) * pow(p,4) * pow((1-p),2)
    N_3 = 360 * choose(n, 6) * pow(p,6) * pow((1-p),9)

    #p1
    x_1 = N_1a + N_1b + N_2a + N_2b +  N_2c + N_3 -\
                          (N_1a*N_1a + N_1b*N_1a + N_2a*N_1a + N_2b*N_1a +  N_2c*N_1a + N_3*N_1a +
                           N_1b*N_1b + N_2a*N_1b + N_2b*N_1b +  N_2c*N_1b + N_3*N_1b +
                            N_2a*N_2a + N_2b*N_2a +  N_2c*N_2a + N_3*N_2a +
                           N_2b*N_2b +  N_2c*N_2b + N_3*N_2b +
                            N_2c*N_2c + N_3*N_2c +
                           N_3*N_3
                           )/m
    edge_num_list.append(x_1)
    OF_list.append(0)
    #p2
    #x_2 = x_1 + 3*N_3line - 6*N_3 - 5 * N_2a - 4 * N_1a
    #edge_num_list.append(x_2)
    #OF_list.append(OF3(n, p) - dis2_relations(n,p))
    #p3
    #x_3 = x_2 + 2*N_2line - 4* N_1b - 4* N_2b - 4*N_2c
    #edge_num_list.append(x_3)
    #OF_list.append(OF3(n, p) - (m - N_3line/12 - N_2line/3))
    #p4
    edge_num_list.append(m)
    OF_list.append(OF3(n, p))

    return edge_num_list, OF_list

def benchmark(n, p):
    #plot  benchmark
    edge_num_list = list()
    OF_list = list()
    p_varient = p
    while p_varient > 0:
        OF = OF3(n, p_varient)
        edge_num_list.append(p_varient * n *(n-1)/2)
        OF_list.append(OF)
        p_varient -= 0.0001
    return edge_num_list, OF_list

def upperlower_plot(n, p):
    list_oracle1_x, list_oracle1_y = oracle_1(n, p)
    list_oracle3_x, list_oracle3_y = oracle_3(n, p)
    list_oracle4_x, list_oracle4_y = motif_expectations.oracle_4(n, p)
    list_oracle5_x, list_oracle5_y = motif_expectations.oracle_5(n, p)
    list_benchmark_x, list_benchmark_y = benchmark(n, p)
    upperlower = plt.subplot(111)
    oracle_line1 = upperlower.scatter(list_oracle1_x, list_oracle1_y,color='red', label="Oracle1")
    oracle_line2 = upperlower.scatter(list_oracle3_x, list_oracle3_y,color='green', label="Oracle3")
    oracle_line3 = upperlower.scatter(list_oracle4_x, list_oracle4_y,color='black', label="Oracle4")
    oracle_line3 = upperlower.scatter(list_oracle5_x, list_oracle5_y,color='purple', label="Oracle5")
    nodes_2 = upperlower.plot(list_benchmark_x,list_benchmark_y, color="blue", label= 'benchmark')
    plt.ylabel('3-hop relations loss')
    #plt.xscale('log')
    plt.xlabel('number of removed edges')
    handles, labels = upperlower.get_legend_handles_labels()
    plt.legend(handles, labels, loc='upper left')
    plt.savefig("plot_bounds.pdf", facecolor='w', edgecolor='w',orientation='portrait')
    plt.show(upperlower)


def diverge_point_plot(n):
    p1 = 0.01
    p2 = 0.02
    p3 = 0.03


    ax = plt.subplot(111)
    e1_xlist = list()
    e1_ylist = list()
    for n_item in range(10, n, 10):
        print n_item
        e1_xlist.append(n_item)
        print motif_expectations.approx1(n_item, p1) - motif_expectations.approx4(n_item, p1)
        e1_ylist.append(motif_expectations.approx1(n_item, p1) - motif_expectations.approx4(n_item, p1))

    e2_xlist = list()
    e2_ylist = list()
    for n_item in range(10, n, 10):
        e2_xlist.append(n_item)
        e2_ylist.append(motif_expectations.approx1(n_item, p2) - motif_expectations.approx4(n_item, p2))

    e3_xlist = list()
    e3_ylist = list()
    for n_item in range(10, n, 10):
        e3_xlist.append(n_item)
        e3_ylist.append(motif_expectations.approx1(n_item, p3) - motif_expectations.approx4(n_item, p3))


    p1, = ax.plot(e1_xlist, e1_ylist, color='red', label="p1 = 0.01")
    p2, = ax.plot(e2_xlist, e2_ylist, color='black', label="p2 = 0.02")
    p3, = ax.plot(e3_xlist, e3_ylist, color='green', label="p3 = 0.03")


    handles, labels = ax.get_legend_handles_labels()
    ax.set_yscale('log')
    ax.legend(handles, labels)
    plt.xlabel("n")
    plt.title("n=" + str(n)+", difference from 4 to 1")
   # plt.show()
    plt.savefig("safeedge_trends_for_p", facecolor='w', edgecolor='w',orientation='portrait')


def diverge_point_plot34(n):
    p1 = 0.001
    p2 = 0.01
    p3 = 0.1


    ax = plt.subplot(111)
    e1_xlist = list()
    e1_ylist = list()
    for n_item in range(10, n, 200):
        print n_item
        e1_xlist.append(n_item)
        e1_ylist.append(  (motif_expectations.approx4(n_item, p1) - motif_expectations.approx1(n_item, p1))/(p1 *n_item* (n_item-1)))

    e2_xlist = list()
    e2_ylist = list()
    for n_item in range(10, n, 200):
        e2_xlist.append(n_item)
        e2_ylist.append(  (motif_expectations.approx4(n_item, p2) - motif_expectations.approx1(n_item, p2))/(p2 *n_item* (n_item-1)))

    e3_xlist = list()
    e3_ylist = list()
    for n_item in range(10, n, 200):
        e3_xlist.append(n_item)
        e3_ylist.append(  (motif_expectations.approx4(n_item, p3) - motif_expectations.approx1(n_item, p3))/(p3 *n_item* (n_item-1)))


    p1, = ax.plot(e1_xlist, e1_ylist, color='red', label="p1 = 0.001")
    p2, = ax.plot(e2_xlist, e2_ylist, color='black', label="p2 = 0.01")
    p3, = ax.plot(e3_xlist, e3_ylist, color='green', label="p3 = 0.1")


    handles, labels = ax.get_legend_handles_labels()
    #ax.set_yscale('log')
    ax.set_xscale('log')
    ax.legend(handles, labels)
    plt.xlabel("n")
    plt.title("n=" + str(n)+", difference from 4 to 1, Normalized")
   # plt.show()
    plt.savefig("safeedge_trends_normalized_41", facecolor='w', edgecolor='w',orientation='portrait')




if __name__ == "__main__":
    #main()
    #plot_np()
    #plot_2appro()

    #for seeing the improvements while gradually removing edges, comparing to random benchmark
    #upperlower_plot(500, 0.004)

    #diverge_point_plot(500)
    diverge_point_plot34(10000)