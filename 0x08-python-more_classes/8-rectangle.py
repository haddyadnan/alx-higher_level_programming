#!/usr/bin/python3

"""
This module defines a rectangle by height and width
"""


class Rectangle:

    """
    class rectangle
    Defining the triangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:

        """
        initialiazing the rectangle class
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):

        """
        print rectangle with character #
        """

        hash = ""
        if (self.__width != 0) and (self.__height != 0):
            sym = str(self.print_symbol)
            hash += "\n".join(sym * self.__width for i in range(self.__height))
        return hash

    def __repr__(self) -> str:

        """
        return string representation of the rectangle
        """
        widstr = str(self.__width)
        heistr = str(self.__height)
        return "Rectangle(" + widstr + ", " + heistr + ")"

    def __del__(self):

        """
        When del instance is invoked
        print message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """
        static method
        Returns: int
            Biggest rectangle based on area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
