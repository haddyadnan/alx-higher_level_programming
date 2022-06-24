#!/usr/bin/python3

"""
This module creates a magic class
    Calculates Circumference and area given radius
    Area:
        calculates area
        self.__radius**2 * math.pi
    circumference:
        return 2 * math.pi * self.__radius
"""

import math


class MagicClass:

    """Class - MagicClass
     Defines a class

    Init instance
         attr: radius
    """

    def __init__(self, radius=0):

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
