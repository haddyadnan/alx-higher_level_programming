#!/usr/bin/python3

import math

"""This module creates a magic class"""


class MagicClass:

    """Class - MagicClass
    Defines a class
    """

    def __init__(self, radius=0):

        """Init instance
        attr: radius
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):

        return self.__radius

    def area(self):
        return self.__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
