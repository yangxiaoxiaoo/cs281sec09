import os
import subprocess

'''
based on the auto-decided block size, fit SBM
distribute into multiple achtung threads
do 3 iterations

on achtung machines, graph data is at net-file-system, while on the decepticons should be new place
'''

def main():
    fin = open("blocknumbers_auto200.txt", 'r')
    Graphnames = list()
    blocksizes = list()
    for line in fin:
        Graphname = line.split(' ')[0]
        blocksize = line.split(' ')[1]
        Graphnames.append(Graphname)
        blocksizes.append(blocksize)

 #   machines = ["achtung%02i" % (x) for x in range(2, 12)]
    machines = ['bonecrusher',
                'hook',
                'longhaul',
                'mixmaster',
                'scrapper',
                'scavenger'
                ]



    while len(Graphnames) >= 1:
        procs = []
        for i, machine in enumerate(machines):
            Graphname1 = Graphnames.pop()
            blocksize1 = blocksizes.pop()
            Graphname2 = Graphnames.pop()
            blocksize2 = blocksizes.pop()
            Graphname3 = Graphnames.pop()
            blocksize3 = blocksizes.pop()
            Graphname4 = Graphnames.pop()
            blocksize4 = blocksizes.pop()
            cmd = ['ssh',
                machine,
                'python',
                '~/graph-models/SBM_fitting.py',
                Graphname1,
                blocksize1,
                   '|',
                   'python',
                '~/graph-models/SBM_fitting.py',
                Graphname2,
                blocksize2,
                   '|',
                   'python',
                '~/graph-models/SBM_fitting.py',
                Graphname3,
                blocksize3,
                   '|',
                   'python',
                '~/graph-models/SBM_fitting.py',
                Graphname4,
                blocksize4,


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