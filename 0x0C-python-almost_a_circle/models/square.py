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

        self.width = self.height = self.size = size

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
                else:
                    self.__dict__["_Rectangle__" + key] = value
        else:
            for i, item in enumerate(args):
                self.__dict__[list(self.__dict__.keys())[i]] = item

    def __str__(self) -> str:
        str_fmt = f"[Square] ({self.id}) {self.x}/{self.y} - "
        str_fmt = str_fmt + str(self.width)
        print(self.__dict__)
        return str_fmt
