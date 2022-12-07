#!/usr/bin/python3
"""takes in an argument and displays all values matches with the argument.
        -take 3 arguments:username, password ,database name and name searched
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
    state_name_searched = sys.argv[4]

    # CONNECT TO MY EXTERN DATABASE
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database_name)
    # ITS A ABSTRACTION
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '%{}%'"
                "ORDER BY id ASC".format(state_name_searched))
    # FOR REMAIMING TUPLE
    result = cur.fetchall()
    for x in result:
        print(x)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
