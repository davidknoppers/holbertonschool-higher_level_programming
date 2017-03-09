#!/usr/bin/python3
"""
Deletes any state that contains an a
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

    for instance in session2.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        session2.delete(instance)
    session.commit()
    session.close()
    db.dispose()
