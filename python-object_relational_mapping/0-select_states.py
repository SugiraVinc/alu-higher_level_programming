#!/usr/bin/python3
"""A module that lists all states from htbn"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # My SQL is running on local  host an dat port 3306
    crd = MySQLdb.connect(user=argv[1], passwd=argv[2], crd=argv[3])
    call = crd.cursor()
    call.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    result = call.fetchall()
    for i in result:
        print(i)
    # close cursor and db
    call.close()
    crd.close()
