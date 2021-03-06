#!/usr/bin/python3
"""
prints some cities and states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities
    JOIN states on cities.state_id = states.id
    ORDER BY cities.id ASC;"""
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
