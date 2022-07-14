#!/usr/bin/python3

"""
This module contains the rectangle class
inherits from base
"""

from models.base import Base


class Rectangle(Base):

    """
    Rectangle class inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """
        inititalize Rectangle class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        defining private instance attribute
        property: width§
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """
        defining private instance attribute
        property: height
        """

        return self.__height

    @height.setter
    def height(self, value):

        """
        defining private instance attribute
        property: height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):

        """
        defining private instance attribute
        property: x
        """

        return self.__x

    @x.setter
    def x(self, value):

        """
        defining private instance attribute
        property: x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):

        """
        defining private instance attribute
        property: y
        """

        return self.__y

    @y.setter
    def y(self, value):

        """
        defining private instance attribute
        property: y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):

        """
        Public instance method: area
        Return: int
            area of rectangle
        """

        return self.__width * self.__height

    def display(self):

        """
        Public instance method: display
        print Rectangle instance to stdout with #
        Return: None
        """

        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self) -> str:

        str_fmt = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
        str_fmt = str_fmt + str(self.__width) + "/" + str(self.__height)
        return str_fmt
