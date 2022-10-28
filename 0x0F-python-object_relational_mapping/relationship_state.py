#!/usr/bin/python3
"""
A python file that contains
the class definition of a State and an instance Base :
If the State object is deleted, all linked City objects
must be automatically deleted. Also, the reference
from a City object to his State should be named state
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):

    """
    State class - Inherits from Base Class
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
