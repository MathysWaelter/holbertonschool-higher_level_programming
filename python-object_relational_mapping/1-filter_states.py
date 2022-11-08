#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
        -take 3 arguments: mysql username, mysql password and database name
        -You must use the module MySQLdb (import MySQLdb)
        -Results must be sorted in ascending order by states.id
        -Results must be displayed as they are in the example below
        -Your code should not be executed when imported"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    # DECLARE MY ARGV FOR EXECUTE IN TERMINAL
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # CONNECT TO MY EXTERN DATABASE
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    # ITS A ABSTRACTION
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'"
                "ORDER BY id ASC")
    # FOR REMAIMING TUPLE
    result = cur.fetchall()
    for x in result:
        print(x)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
