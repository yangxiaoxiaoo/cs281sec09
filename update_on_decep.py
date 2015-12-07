'''
usage: python update_on_decep.py graph_models.py
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



if __name__ == "__main__":
    main(sys.argv[1])