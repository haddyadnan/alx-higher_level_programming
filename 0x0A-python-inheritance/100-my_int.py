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

        self.num = value

    def __eq__(self, other):

        """
        Invert __eq__
        """

        return self.num != other

    def __ne__(self, other):

        """
        Invert __ne__
        """

        return self.num == other
