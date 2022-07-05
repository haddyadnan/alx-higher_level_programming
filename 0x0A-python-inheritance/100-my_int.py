#!/usr/bin/python

"""
This module contains a class MyInt that inherits from int
"""


class MyInt(int):

    """
    Class MyInt
    Inherits from int
    """

    def __init__(self, value):

        """
        Instantiate class
        """

        self.value = value

    def __eq__(self, other):

        """
        Invert __eq__
        """

        return self.value != other

    def __ne__(self, other):

        """
        Invert __ne__
        """

        return self.value == other
