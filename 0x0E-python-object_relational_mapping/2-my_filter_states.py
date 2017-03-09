#!/usr/bin/python3
"""
prints states that match a given input
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    input_state = sys.argv[4]
    query = """SELECT id, name FROM states WHERE name="{:s}"
    ORDER BY id ASC;""".format(input_state)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
