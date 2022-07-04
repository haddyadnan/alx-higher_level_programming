#!/usr/bin/python3

"""
This module return True if object is exactly\
an instance of a specified class
"""


def is_same_class(obj, a_class):

    """
    Return True if obj is an instance of a_class
    """

    return type(obj).__name__ == a_class.__name__
