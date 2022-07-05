#!/usr/bin/python3

"""
This module adds a new attribute to an object if possible
"""


def add_attribute(*args):

    """
    add attribute to object args[0]
    """

    attr = getattr(args[0], "__doc__", None)
    if attr is None:
        setattr(*args)
    else:
        raise TypeError("can't add new attribute")
