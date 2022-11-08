#!/usr/bin/python3
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
    print(x)

# TEST WITH FETCHONE
# print ("(%s, '%s')" % cur.fetchone())
# RESULT :
# (1, 'California')

# Close all cursors
cur.close()
# Close all databases
db.close()