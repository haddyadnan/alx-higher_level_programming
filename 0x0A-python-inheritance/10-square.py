#!/usr/bin/python3

"""
This module contains class Square that inherits from 9-rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """
    Class Square
    Inherits from Rectangle
    """

    def __init__(self, size) -> None:

        """
        class Square Instantiation
        """
        Rectangle.__init__(self, size, size)
