#!/usr/bin/python3

"""
This module creates an object from a json file
"""


import json


def load_from_json_file(filename):

    """
    creates an object from json file
    """

    with open(filename, "r") as f:

        return json.loads(f.read())
