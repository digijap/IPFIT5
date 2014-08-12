import sqlite3
import os

_DATABASE = "/home/jasper/IPFIT5/file.db" #Waar staat de database
  
def setupConnection(db = _DATABASE):
    #Con is connectie naar de database. 
    #Cur is waar ga je de data invoegen in de database. De cursor van de database
    con = sqlite3.connect(db)
    cur = con.cursor()
    return cur,  con
    
def setupDatabase(clearDB, db = _DATABASE):
    makeTable = "CREATE TABLE files(ID INT, Path TEXT, Filename TEXT, Extension VARCHAR(10), Mime TEXT, md5 VARCHAR(32))"
    #Maak database aan als die nog niet bestaat. Legt anders de connectie naar de database en maakt de tabel

    if not os.path.isfile(db):
        #Als de database nog niet bestaat leg dan de connectie en dan wordt de database aangemaakt.
        cur,  con = setupConnection(db)
        cur.execute(makeTable)
    elif os.path.isfile(db) and clearDB:
        cur,  con = setupConnection(db)
        cur.execute("DROP TABLE files")
        cur.execute(makeTable)

def updateDatabase(ID,  Path,  Filename,  Extension,  MD5, magic,  db = _DATABASE):
    cur,  con = setupConnection(db)
    command = 'INSERT INTO files VALUES( %d,%s, %s, %s, %s, %s)' % (ID,   "'"+ Path+"'", "'"+Filename+"'","'"+Extension+"'",   "'"+magic+"'", "'"+MD5+"'")
    cur.execute(command)
    con.commit()
