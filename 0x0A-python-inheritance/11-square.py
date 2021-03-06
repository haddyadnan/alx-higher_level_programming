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
        super().__init__(size, size)

    def __str__(self) -> str:

        """
        return Square description
        """
        return f"[Square] {str(self.__width__)}/{str(self.__height__)}"
