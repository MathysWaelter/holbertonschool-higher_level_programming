#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:
        -Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
        -You must use the module MySQLdb (import MySQLdb)
        -Your script should connect to a MySQL server running on localhost at port 3306
        -Results must be sorted in ascending order by states.id
        -Results must be displayed as they are in the example below
        -Your code should not be executed when imported"""

import MySQLdb
import sys

# DECLARE MY ARGV FOR EXECUTE IN TERMINAL
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

# CONNECT TO MY EXTERN DATABASE 
db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database_name)
# ITS A ABSTRACTION
cur = db.cursor()
cur.execute("SELECT * FROM states")
# FOR REMAIMING TUPLE    
result = cur.fetchall()
for x in result:
    print(x )

# TEST WITH FETCHONE
# print ("(%s, '%s')" % cur.fetchone())
# RESULT :
# (1, 'California')

# Close all cursors
cur.close()
# Close all databases
db.close()