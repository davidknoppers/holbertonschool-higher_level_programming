#!/usr/bin/python3
"""
New Orleans is awesome, so let's add Louisiana to the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    db = create_engine(engine)
    Base.metadata.create_all(db)
    session1 = sessionmaker(bind=db)
    session2 = session1()

    la = State(name='Louisiana')
    session2.add(la)
    session2.commit()
    instance = session2.query(State).filter_by(name="Louisiana").first()
    print("{}".format(added.id()))
