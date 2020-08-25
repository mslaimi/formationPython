import os
import sqlite3

db_name="formation.db"
db_is_new= not os.path.exists(db_name)
conn=sqlite3.connect(db_name)
if db_is_new:
    print ("creating db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE personnes (id INTEGER PRIMARY KEY AUTOINCREMENT , nom TEXT, prenom TEXT)")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('doe','john')")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('snow','jon')")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('wick','john')")
else :
    print ("db exists")
    cur = conn.cursor()
    cur.execute("CREATE TABLE personnes (id INTEGER PRIMARY KEY AUTOINCREMENT , nom TEXT, prenom TEXT)")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('doe','john')")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('snow','jon')")
    cur.execute("INSERT INTO personnes (nom,prenom) VALUES ('wick','john')")
conn.close()
