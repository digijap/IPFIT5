import os.path
import sys

from subprocess import check_output


sourcedir = sys.argv[1]


for dirpath, dirnames, filenames in os.walk(sourcedir):
    for filename in filenames:
        if not filename.endswith(".rst"):
            continue
            
        filepath = os.path.join(dirpath, filename)
        
        out = check_output(['hg', 'log', '-l1', '--template',
                        '{date|hgdate} {rev}',
                        filepath,
                        ])
        print filepath, out
