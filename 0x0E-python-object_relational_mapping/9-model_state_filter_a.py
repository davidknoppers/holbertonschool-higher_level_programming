#!/usr/bin/python3
"""
list objects from hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                              sys.argv[2],
                                                              sys.argv[3])
    db = create_engine(engine)

    Base.metadata.create_all(db)
    session1 = sessionmaker(bind=db)
    session2 = session1()

    for instance in session2.query(State).order_by(State.id):
        if 'a' in instance.name:
            print("{}: {}".format(instance.id, instance.name))
