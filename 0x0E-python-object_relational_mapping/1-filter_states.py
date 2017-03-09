#!/usr/bin/python3
# prints states that start with N
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306, host="localhost")
    cursor = db.cursor()

    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id asc;"

    cursor.execute(query)

    for row in cursor.fetchall():
        if row[1][0] == "N":
            print(row)

    cursor.close()
    db.close()
