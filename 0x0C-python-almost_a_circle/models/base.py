#!/usr/bin/python3

"""
This module contains the Base class of all other classes in the project
"""


class Base:

    """
    Base class for other classses
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:

        """
        init the base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
