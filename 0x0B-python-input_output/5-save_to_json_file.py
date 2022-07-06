#!/usr/bin/python3

"""
This module writes an Object to a text file, using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):

    """
    write an Object to a text file
    with json representation
    """

    with open(filename, "w") as f:

        f.write(json.dumps(my_obj))
