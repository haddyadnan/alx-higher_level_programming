#!/usr/bin/python3

"""
This module contains the square class
inherits from base
"""

from models.rectangle import Rectangle

class Square(Rectangle):

    """
    Rectangle class inherits from Base class
    """
    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)

    @property
    def size(self):

        """
        defining private instance attribute
        property: size
        """

        return self.width

    @size.setter
    def size(self, value):

        """
        defining private instance attribute
        setter: size
        """

        self.width = value
        self.height = value

    def __str__(self) -> str:
        str_fmt = f"[Square] ({self.id}) {self.x}/{self.y} - "
        str_fmt = str_fmt + str(self.width)
        return str_fmt