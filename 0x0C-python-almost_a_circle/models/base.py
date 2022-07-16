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

    @classmethod
    def save_to_file(cls, list_objs):

        """
        write json string of list_objs to a file
        """

        lst_obj = []
        if list_objs is not None:
            for objs in list_objs:
                t_dict = cls.to_dictionary(objs)
                lst_obj.append(t_dict)
            t_json = cls.to_json_string(lst_obj)
        else:
            t_json = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            num = f.write(t_json)

    @staticmethod
    def from_json_string(json_string):

        """
        returns list of json string representation of json_string
        """

        return json.loads(json_string)