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

    n = 20
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
    plt.title("n=20, 1-order approxamation")
    plt.subplot(212)
    Error1_2 = N_1a + N_1b + N_2a + N_2b + N_2c + N_3
    plt.plot(p, Error1_2)
    plt.xlabel("p")
    plt.title("n=20, 1-/2- error")

    '''
    plt.subplot(221)
    plt.plot(p, N_3line)
    plt.title("N_3line")

    plt.subplot(222)
    plt.plot(p, N_2line)
    plt.title("N_2line")

    plt.subplot(223)
    plt.plot(p, N_1a)
    plt.title("N_1a")

    plt.subplot(224)
    plt.plot(p, N_1b)
    plt.title("N_1b")


    plt.subplot(221)
    plt.plot(p, N_2a)
    plt.title("N_2a")

    plt.subplot(222)
    plt.plot(p, N_2b)
    plt.title("N_2b")

    plt.subplot(223)
    plt.plot(p, N_2c)
    plt.title("N_2c")

    plt.subplot(224)
    plt.plot(p, N_3)
    plt.title("N_3")
'''

    plt.show()

if __name__ == "__main__":
    #main()
    plot_np()