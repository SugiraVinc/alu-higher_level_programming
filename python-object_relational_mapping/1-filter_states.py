#!/usr/bin/python3
"""module to list states starting with N"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    result = cur.fetchall()
    # Displaying names starting with N
    for i in result:
        if i[1][0] == 'N':
            print(i)
    # closing the fetch
    cur.close()
    db.close()
