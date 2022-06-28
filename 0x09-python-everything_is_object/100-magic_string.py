#!/usr/bin/python3

"""A function that returns a string "BestSchool
   n times the number of iteration
"""


def magic_string():

    """
    Magic String:
    """

    magic_string.counter = getattr(magic_string, "counter", 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.counter)])
