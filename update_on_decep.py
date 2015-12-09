'''
usage: python update_on_decep.py graph_models.py
for uppdating code on decepticons
alter_usage: reading the otput file of SBM_fitting and see how many of them finished
'''

import sys
import subprocess

def main(file_name):
    machines = ['bonecrusher',
                'hook',
                'longhaul',
                'mixmaster',
                'scrapper',
                'scavenger'
                ]
    for machine in machines:
        subprocess.check_call(
            "scp " + "~/facebook/sparsify/cs281sec09/" + file_name +" " + "xiaofeng@"+ machine + ":~/graph-models/",
            shell=True)


def check_fit_results():
    machines = ['bonecrusher',
                'hook',
                'longhaul',
                'mixmaster',
                'scrapper',
                'scavenger'
                ]
    for machine in machines:
        subprocess.check_call(
            "ssh " + machine + "cd ~/graph-models/" + "ls",
            shell=True)


if __name__ == "__main__":
   # main(sys.argv[1])
    check_fit_results()
