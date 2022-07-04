#!/usr/bin/python3

"""
This module return True if object is an instance of\
or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):

    """
    Return True if obj is an instance or inherits from a_class
    """

    return isinstance(obj, a_class)
