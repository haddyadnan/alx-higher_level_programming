#!/usr/bin/python3

"""
A script that lists all State objects that contain arg passed
from the database passed by argument
"""

import sys

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    arg = sys.argv[4].split()[0]  # SQL INJECTION WALKAROUND
    query = session.query(State).filter(State.name.ilike(arg)).all()
    if query:
        for state in query:
            print(f"{state.id}")
    else:
        print("Not found")
