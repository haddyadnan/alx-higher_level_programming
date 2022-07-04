#!/usr/bin/python3

"""
This module return True if object is an instance of
a class that inherited [directly or indirectly from a specified class
"""


def inherits_from(obj, a_class):

    """
    Return True if obj is an instance or inherits from a_class
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
