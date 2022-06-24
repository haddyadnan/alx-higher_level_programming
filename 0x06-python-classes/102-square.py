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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """
        Public Instance method of class square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public Instance method of class square
        """

        return self.__size * self.__size

    def __lt__(self, other):

        """Magic Method:  <"""

        return self.__size < other.size

    def __le__(self, other):

        """Magic Method <="""

        return self.__size <= other.size

    def __eq__(self, other):

        """Magic Method =="""

        return self.__size == other.size

    def __ne__(self, other):

        """Magic Method !="""

        return self.__size != other.size

    def __gt__(self, other):

        """Magic Method >"""

        return self.__size > other.size

    def __ge__(self, other):

        """Magic Method >="""

        return self.__size >= other.size
