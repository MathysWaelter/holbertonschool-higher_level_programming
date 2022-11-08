#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name)

cur = db.cursor()
cur.execute("SELECT * FROM states")
result = cur.fetchall()
for x in result:
    print(x )

cur.close()

db.close()
