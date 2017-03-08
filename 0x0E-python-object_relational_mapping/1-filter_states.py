#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
cursor = db.cursor()

query = ("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id asc;")

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

db.close()
