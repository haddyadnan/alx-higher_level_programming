#!/usr/bin/python3

"""
This module defines a rectangle by height and width
"""


class Rectangle:

    """
    Instantiating a rectangle class
    """

    def __init__(self, width=0, height=0) -> None:

        self.width = width
        self.height = height

    @property
    def width(self):

        """
        defining private instance attribute
        property: width
        """

        return self.__width

    @width.setter
    def width(self, value):

        """
        setting private instance attribute - width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """
        definig private instance attribute
        property: height
        """

        return self.__height

    @height.setter
    def height(self, value):

        """
        Setting private instance attribute - height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """
        Public instance method: area
        Return: int
            area of rectangle
        """

        return self.__width * self.__height

    def perimeter(self):

        """
        Public instance method: perimeter
        Return: int
            perimeter of rectangle
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (self.__height + self.width) * 2
