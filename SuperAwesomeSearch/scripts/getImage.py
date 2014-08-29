import os
import sys

path = sys.argv[1]

casenumber = "001" #-C
description = "zwarte usb" #-D
examiner = "Jasper Jansen" #-e
evidencenumber = "001" #-E
mediatype = "removable" #-m KIEZEN UIT fixed removable optical memory
mediaflags = "logical" #-M logical of physical
notes = "test" # -n
pathforimage = "/home/jasper/usb" #-t


#Dit kan ik pas gebruiken als er een sleutel is voor nu regelt ewfacquire dit zelf
"""command = ("ewfacquire {0} -b 64 -c fast -C {1}"
            " -e {2} -E {3} -D {4}"
            " -m {5} -M {6} -N {7}"
            " -t {8} -g 64 -S 8GiB -u"
            )
#command = command.format(path, casenumber, examiner, evidencenumber, evidencenumber, mediatype, mediaflags, notes, pathforimage)"""

command = "ewfacquire " + path

term = "lxterminal -e '" + command + "'"

os.system(term)
