#!/usr/bin/python3
""" Connecting a class to MySQL"""

import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                              sys.argv[2],
                                                              sys.argv[3])
    db = create_engine(engine)
    Base.metadata.create_all(db)
    session1 = sessionmaker(bind=db)
    session2 = session1
    try:
        instance = sesh2.query(State).first()
        print("{}: {}".format(instance.id, instance.name))
    except:
        print("Nothing")
