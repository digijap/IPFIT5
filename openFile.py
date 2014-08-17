#OpenFile
from sys import argv

script = argv[0]
filename = argv[0]

txt = open(filename)

print "Open file %r:" % filename
# Het is alleen magelijk om de file te lezen
print txt.read()

print "Type the filename again:"
#kies zelf een file die je wil openen
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
