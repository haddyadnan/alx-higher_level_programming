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

        self.__y = value


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
