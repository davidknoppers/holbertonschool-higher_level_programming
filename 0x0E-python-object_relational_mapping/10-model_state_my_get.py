#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
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

    state_name = sys.argv[4]
    for instance in session2.query(State).filter(State.name == state_name):
        print(instance.id)
        sys.exit(1)
    print("Not found")
