#!/usr/bin/python3
"""Write a script that lists all cities of that state,
    -take 4 arguments: username, password, database name and state name
    -You must use the module MySQLdb (import MySQLdb)
    -Results must be sorted in ascending order by cities.id
    -You can use only execute() once
    -Results must be displayed as they are in the example below
    -Your code should not be executed when imported"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    # DECLARE MY ARGV FOR EXECUTE IN TERMINAL
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # CONNECT TO MY EXTERN DATABASE
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    # ITS A ABSTRACTION
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
            LEFT JOIN states ON states.id = cities.state_id
            WHERE states.name = %s ORDER BY cities.id ASC""", (state_name,))
    # FOR REMAIMING TUPLE
    result = cur.fetchall()

    # PRINT RESULT IN STRING 
    citi = ""
    virgule = ""
    for x in result:
        citi = citi + virgule + x[0]
        virgule = ", "
    print (citi)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
