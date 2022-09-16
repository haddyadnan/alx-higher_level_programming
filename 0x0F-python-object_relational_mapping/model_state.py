#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance Base :
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    State class - Inherits from Base Class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
