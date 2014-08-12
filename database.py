import sqlite3

con = sqlite3.connect("/home/jasper/IPFIT5/file.db")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE File(ID INT, Path TEXT, Filename TEXT, Extension TEXT, md5 VARCHAR(32))")
