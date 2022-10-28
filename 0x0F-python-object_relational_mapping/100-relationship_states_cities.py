#!/usr/bin/python3
#!/usr/bin/python3

"""
Write a script that deletes all State objects
with a name containing the letter a
from the database passed
"""


import sys
from unicodedata import name
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

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

    state = State(name="California")
    city = City(name="San Francisco")

    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
