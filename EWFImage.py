import os

path = "/dev/sda1"

casenumber = "001" #-C
description = "zwarte usb" #-D
examiner = "Jasper Jansen" #-e
evidencenumber = "001" #-E
mediatype = "removable" #-m KIEZEN UIT fixed removable optical memory
mediaflags = "logical" #-M logical of physical
notes = "test" # -n
pathforimage = "/home/jasper/usb" #-t


command = ("ewfacquire %s -c fast -C %s"
            " -e %s -E %s -D %s"
            " -m %s -M %s -N %s"
            " -t %s -S 8GiB -u"
            ) %path ,%casenumber, %examiner, %evidencenumber, %description, %mediatype, %mediaflags, %notes, %pathforimage

term = "lxterminal -e '" + command + "'" #command voor opstarten terminal

if os.getuid() != 0: #check of je root bent of niet
    print "Je bent niet root"
else:
    os.system(term) 
