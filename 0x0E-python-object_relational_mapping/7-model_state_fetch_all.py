#!/usr/bin/python3
""" Connecting a class to MySQL"""

import sys
import sqlalchemy
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                                      .format(sys.argv[1],
                                              sys.argv[2], sys.argv[3]))
    query = "SELECT * FROM states"
    result = engine.execute(query)
    for row in result:
        temp = str(row[0]) + ":" + " " + row[1]
        print(temp)
