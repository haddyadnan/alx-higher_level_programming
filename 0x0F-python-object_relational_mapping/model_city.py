#!/usr/bin/python3
"""
A python file that contains
the class definition of a State and an instance Base :
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from model_state import State, Base

Base = declarative_base()


class City(Base):

    """
    State class - Inherits from Base Class
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
