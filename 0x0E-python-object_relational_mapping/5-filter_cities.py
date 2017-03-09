#!/usr/bin/python3
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    input_state = sys.argv[4]
    input_state = input_state.split(';')
    input_state = input_state[0]

    query = """SELECT cities.name FROM cities
    JOIN states on cities.state_id = states.id
    WHERE states.name = '{:s}'
    ORDER BY cities.id ASC""".format(input_state)
    cursor.execute(query)

    result = []
    for row in cursor.fetchall():
        result.append(row[0])
        print(', '.join(result))
    cursor.close()
    db.close()
