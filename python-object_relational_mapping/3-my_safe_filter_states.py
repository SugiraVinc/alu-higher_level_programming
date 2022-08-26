#!/usr/bin/python3
"""Module to retrive data from table"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # local host and port 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # usual SQL querry
    cur.execute("SELECT * FROM states WHERE states.name = %s\
    ORDER BY states.id ASC", (argv[4],))
    result = cur.fetchall()
    # Is name same as passed in the argument
    for i in result:
        print(i)
    cur.close()
    db.close()
