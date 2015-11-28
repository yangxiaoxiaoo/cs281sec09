import os
import subprocess

'''
based on the auto-decided block size, fit SBM
distribute into multiple achtung threads
do 3 iterations
'''

def main():
    fin = open("blocknumbers_auto200.txt", 'r')
    Graphnames = list()
    blocksizes = list()
    for line in fin:
        Graphname = line.split(' ')[0]
        blocksize = int(line.split(' ')[1])
        Graphnames.append(Graphname)
        blocksizes.append(blocksize)

    machines = ["achtung%02i" % (x) for x in range(2, 12)]



    while len(Graphnames) >= 1:
        procs = []
        for i, machine in enumerate(machines):
            Graphname = Graphnames.pop()
            blocksize = blocksizes.pop()
            cmd = ['ssh',
                machine,
                'python',
                '/home/xiaofeng/facebook/sparsify/cs281sec09/SBM_fitting.py',
                Graphname,
                blocksize
                ]
            procs.append(subprocess.Popen(cmd))

        for proc in procs:
            proc.wait()


def testrun():
    #test run on machines to see if queue works
    #passed
    machines = ["achtung%02i" % (x) for x in range(2, 12)]

    list = [1,2,3,4,5,6,7, 8,9,10,11,12,13,14,15,16,17]

    while len(list) >= 1:
        procs = []
        for i, machine in enumerate(machines):
            index = list.pop()
            print "in cmd there will be :" + str(index)
            cmd = ['ssh',
                machine,
                'python',
                '/home/xiaofeng/facebook/sparsify/cs281sec09/SBM_fitting.py'
                ]
            procs.append(subprocess.Popen(cmd))

        for proc in procs:
            proc.wait()

        print len(list)


if __name__ == "__main__":
    main()


   # testrun()