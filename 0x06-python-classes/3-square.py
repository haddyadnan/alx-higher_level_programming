#!/usr/bin/python3

""" Class square that defines a class based on 2-square.py"""


class Square:
    """
    Class - Square
    Defines a square
    """

    def __init__(self, size=0):
        """
        Square Instance
        Private instance attribute: __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Public Instance method of class square
        """
        return self.__size * self.__size
