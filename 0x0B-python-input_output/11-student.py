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

    def to_json(self, attrs=None):

        """
        public attribute:
        to_json
        Retrives dictionary representation of class Student
        """

        info = {}
        if type(attrs) == list:
            for attr in attrs:
                if attr in list(self.__dict__.keys()):
                    value = getattr(self, attr)
                    info[attr] = value
            return info
        return self.__dict__

    def reload_from_json(self, json):

        """
        public attribute:
        reload from json
        replaces all attributes of the Student class
        """
        if json:
            self.age = json["age"]
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
        return self


# j_student_1 = {"first_name": "John", "last_name": "Lot", "age": 45}
# new_student_1 = Student("Fake", "Fake", 89)
# new_student_1.reload_from_json(j_student_1)
# print(new_student_1)
# print(type(new_student_1))
# # print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
