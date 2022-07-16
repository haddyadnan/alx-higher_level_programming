#!/usr/bin/python3

"""
This module contains the Base class of all other classes in the project
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):

        """
        returns JSON string representation of list_dictiomaries
        """

        if list_dictionaries is None or any(list_dictionaries) is False:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
