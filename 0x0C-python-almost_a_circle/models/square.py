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

    def update(self, *args, **kwargs):

        """
        Public instance method: update
        update class attribute
        Return: self
        """

        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.__dict__[key] = value
                elif key == "size":
                    self.__dict__["_Rectangle__width"] = value
                else:
                    self.__dict__["_Rectangle__" + key] = value
        else:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                elif i == 1:
                    self.size = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value

    def __str__(self) -> str:

        str_fmt = f"[Square] ({self.id}) {self.x}/{self.y} - "
        str_fmt = str_fmt + str(self.size)
        return str_fmt
