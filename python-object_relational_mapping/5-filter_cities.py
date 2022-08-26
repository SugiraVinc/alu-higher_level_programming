#!/usr/bin/python3
"""Module to retrive data from table"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # local host and port 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # usual SQL querry to link tables based on state_id
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC""", (argv[4],))
    result = cur.fetchall()
    cities = []
    # Is name same as passed in the argument
    for i in result:
        if i[2] == argv[4]:
            cities.append(i[1])
    print(', '.join(cities))
    cur.close()
    db.close()
