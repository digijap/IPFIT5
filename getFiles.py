import os
import sqlite3
import hashlib
from database import updateDatabase,  setupDatabase

#Voor het berekenen van de tijd hoelang het programma bezig is
import time

#Klaar  198419 Bestanden geindexd
#1908.73631406 seconden

clearDB = True
directory = "/home" #Voor de file listing

start_time = time.time()

def getFileList(fp):
    count = 0 #Primary key voor database
    euid = os.geteuid()     #EUID is 0 als je root bent anders kan het script niet uitgevoerd worden
    
    if euid != 0:
        print "You are not root"
        exit()
    else:
        setupDatabase(clearDB)
        if os.path.exists(fp):
            try:
                #Loop door alle folder en filenames heen
                for dirname, dirnames, filenames in os.walk(fp):
                    for filename in filenames:
    
                        #Get extension als de extension 1 of 0 lang is dan is er geen extensie
                        #Dit returnt van test.txt    fname = test    extension = .txt
                        fname,  extension = os.path.splitext(filename) 
                        if len(extension) <= 1:
                            extension = "None"
                        
                        #Get MD5 van de functie MD5sum
                        md5 = md5sum(dirname+"/"+filename)
                        
                        #De count met 1 verhogen voor de primary key
                        count += 1
                        
                        updateDatabase(count,  dirname,  fname,  extension,  md5)
            except Exception,  e:
                print "Er is een fout opgetreden: ",  e
    return count
    
def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "r+b") as f:
        #als block size is bereikt in f dan geeft lambda de text terug en wordt de hash geupdate
        for block in iter(lambda: f.read(blocksize), ""): 
            hash.update(block)
    #return de hash waarde
    return hash.hexdigest()


count = getFileList(directory)

#Hoelang doet het programma erover
print count,  "Bestanden geindexeert",  round(count / (time.time() - start_time)),  'per seconde'
