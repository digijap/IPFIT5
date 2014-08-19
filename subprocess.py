#image
import subprocess

# Probeer eerst sudo ewfacquire /dev/sdb  in de terminal, run daarna de code, dan zie je waar ik op vastloop.

command = "sudo ewfacquire /dev/sdb" # the shell command creates image
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

output = process.communicate()

print output[0]

# Je kan ook andere commands gebruiken:
# sudo md5sum /dev/sdb
# ls -lh
# ewfinfo imagename.e01 
# ewfverify imagename.eo1

# sudo ewfacquire /dev/sdb </where/you/want/filename.txt , maakt een file met de informatie uit de terminal.

