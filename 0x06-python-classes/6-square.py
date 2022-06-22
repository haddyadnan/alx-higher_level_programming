#!/usr/bin/python3

""" Class square that defines a class based on 2-square.py"""


class Square:
    """
    Class - Square
    Defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Square Instance
        Private instance attribute: __size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):

        """
        Private Instance attribute - position
        property
        """

        return self.__position

    @position.setter
    def position(self, position):

        """
        Private instance attribute - position
        Setter - to set it
        """

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Public Instance method of class square
        """

        return self.size * self.size

    def my_print(self):

        """
        Public Instance method of class square - prints stdout
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
