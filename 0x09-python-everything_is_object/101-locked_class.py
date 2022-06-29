#!/usr/bin/python3

"""
This module creates a locked class
Prevents user from dynamically creating new instance attributes
except if the attribute is called first name
"""


class LockedClass:

    """
    Locked class
    Dynamic Attribute:
        first_name
    """

    __slots__ = "first_name"
