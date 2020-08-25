import os
import sqlite3

db_name="formation.db"
db_is_new= not os.path.exists(db_name)
conn=sqlite3.connect(db_name)
if db_is_new:
    print ("creating db")
else :
    print ("db exists")
conn.close()
