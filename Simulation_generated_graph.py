#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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

    for n in (range(1,100) + range(1,Nmax,100)):

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

        p_diverge = 0
        for i in range(1, len(p)):
            if Appx3[i] > float(1 + error)*Appx1[i]:
                p_diverge = p[i]
                print i
                break
        N_list.append(n)
        P_list.append(p_diverge)

    return N_list, P_list



if __name__ == "__main__":
    #main()
    #plot_np()
    plot_2appro()