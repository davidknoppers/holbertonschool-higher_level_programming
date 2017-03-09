#!/usr/bin/python3
# like 3, but with sanitized inputs
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    input_state = sys.argv[4]
    input_state = input_state.split(';')
    input_state = input_state[0]

    query = """SELECT id, name FROM states WHERE name="{:s}"
    ORDER BY id ASC;""".format(input_state)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
