#!/usr/bin/python3

"""
This module contains a class Student
"""


class Student:

    """
    Class Student
    """

    def __init__(self, first_name, last_name, age) -> None:
        """
        Class Student - Instantiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """
        public attribute:
        to_json
        Retrives dictionary representation of class Student
        """
        return self.__dict__
