#!/usr/bin/python3

"""
This module contains class Rectangle that inherits from 7-base_geometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """
    class Rectangle
    """

    def __init__(self, width, height) -> None:

        """
        class rectangle instantiation
        width, height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width__ = width
        self.__height__ = height

    def area(self):

        """
        Public Instance - area
        calculate area
        """

        return self.__width__ * self.__height__

    def __str__(self) -> str:

        """
        return rectangle description
        """
        return f"[Rectangle] {str(self.__width__)}/{str(self.__height__)}"
