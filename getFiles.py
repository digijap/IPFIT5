import os
import sqlite3
import hashlib
#Voor het berekenen van de tijd hoelang het programma bezig is
import time
import math

#Klaar  198419 Bestanden geindexd
#1908.73631406 seconden

#----------------------------------------------------------------------------------------- #
#DATABASE CONNECTIE WORDT GESLOTEN IN getFileList#
#-----------------------------------------------------------------------------------------#

_DATABASE = "/home/jasper/IPFIT5/file.db" #Waar staat de database
directory = "/home" #Voor de file listing
ClearDB = False 

start_time = time.time()


def setupDatabase(db):
    #Con is connectie naar de database. 
    #Cur is waar ga je de data invoegen in de database. De cursor van de database
    #Maak database aan als die nog niet bestaat. Legt anders de connectie naar de database
    if ClearDB:
        con = sqlite3.connect(db)
        cur = con.cursor() 
        cur.execute("DROP TABLE File")
        cur.execute("CREATE TABLE File(ID INT, Path TEXT, Filename TEXT, Extension TEXT, md5 VARCHAR(32))")
    
    if not os.path.isfile(db):
        con = sqlite3.connect(db)
        cur = con.cursor() 
        cur.execute("CREATE TABLE File(ID INT, Path TEXT, Filename TEXT, Extension TEXT, md5 VARCHAR(32))")

def getFileList(fp):
    count = 0 #Primary key voor database
    con = sqlite3.connect(_DATABASE)
    cur = con.cursor() 
    
    #EUID is 0 als je root bent anders kan het script niet uitgevoerd worden
    euid = os.geteuid()
    if euid != 0:
        print "Youre not root"
        exit()
    else:
        if os.path.exists(fp):
            try:
                for dirname, dirnames, filenames in os.walk(fp):
                    for filename in filenames:
                        count += 1
                        
                        
                        filen,  extension = os.path.splitext(filename)
                        if len(extension) <= 1:
                            extension = "None"
                        
                        md5 = md5sum(dirname+"/"+filename)
                        
                        md5sum(dirname+"/"+filename)
                        
                        #Insert de data die wordt op gegeven door de OS.walk in de database.
                        command = 'INSERT INTO File VALUES( %d,%s, %s, %s, %s)' % (count,   "'"+ dirname+"'", "'"+filen+"'","'"+extension+"'",  "'"+md5+"'")
    
                        #print command
                        cur.execute(command)
                        #Schrijf de data weg
                        con.commit()
            except Exception,  e:
                print "Er is een fout opgetreden",  e
    #Sluit de database connectie
    con.close()
    
    return count
    
def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "r+b") as f:
        for block in iter(lambda: f.read(blocksize), ""):
            hash.update(block)
    return hash.hexdigest()




setupDatabase(_DATABASE)
count = getFileList(directory)

#Hoelang doet het programma erover
print count,  "Bestanden geindexeert",  round(count / (time.time() - start_time)),  'per seconde'
