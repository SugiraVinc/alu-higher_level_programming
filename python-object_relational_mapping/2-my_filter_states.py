#!/usr/bin/python3
"""Module that retrieve database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Usual SQL querry
    cur.execute("SELECT * FROM states WHERE states.name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))
    result = cur.fetchall()
    # Navigating through the arguments
    for i in result:
        if i[1] == argv[4]:
            print(i)
    # close cursor and db
    cur.close()
    db.close()
