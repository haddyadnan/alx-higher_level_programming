#!/usr/bin/python3

"""
Class base Geometry based on 6-base_geometry
"""


class BaseGeometry:

    """
    Base Geometry class
    """

    def area(self):

        """
        Public instance of BG
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Public instance - integer_validator
        validates value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
