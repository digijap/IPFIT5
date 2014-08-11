import sqlite3

count = 3
dirname = '/home/jasper'
filename = 'picture.jpg'
con = sqlite3.connect("/home/jasper/IPFIT5/file.db")


#command = 'INSERT INTO File VALUES( %d,%s, %s)' % (count,  "'"+ dirname+"'", "'"+filename+"'")

cur = con.cursor()
#cur.execute(command)

con.commit()
cur.execute("SELECT * FROM file")
rows = cur.fetchall()

for row in rows:
    print row

con.close()
