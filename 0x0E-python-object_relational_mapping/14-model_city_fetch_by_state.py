#!/usr/bin/python3
"""
Like number 7 for cities
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import cities
if __name__ == "__main__":
    engine = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    db = create_engine(engine)
    Base.metadata.create_all(db)
    session1 = sessionmaker(bind=db)
    session2 = session1()

    for instance in session2.query(State.name, City.id, City.name).filter(
            State.id == City.state.id).order_by(City, id):
        print("{}: {{}} {}".format(instance[0], instance[1], instance[2]))
    session2.commit()
    session2.close()
    db.dispose()
