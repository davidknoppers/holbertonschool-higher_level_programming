#!/usr/bin/python3
"""
prints all states
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()

    query = ("SELECT id, name FROM states ORDER BY states.id asc;")

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    db.close()
