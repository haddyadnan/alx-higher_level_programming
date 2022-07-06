#!/usr/bin/python3

"""
This module contains a class Student
"""

import os
import sys

read_file = __import__("0-read_file").read_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)


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

        self.age = json["age"]
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]

        return self.__dict__


# student_1 = Student("John", "Doe", 23)
# j_student_1 = student_1.to_json()
# print("Initial student:")
# print(student_1)
# print(type(student_1))
# print(type(j_student_1))
# print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


# save_to_json_file(j_student_1, path)
# read_file(path)

# print("\n\n\nThis is for fake\n")
# print("Fake student:")
# new_student_1 = Student("Fake", "Fake", 89)
# print(new_student_1)
# print(type(new_student_1))
# print(
#     "{} {} {}".format(
#         new_student_1.first_name, new_student_1.last_name, new_student_1.age
#     )
# )


# print("After this")
# print("Load dictionary from file:")
# new_j_student_1 = load_from_json_file(path)

# new_student_1.reload_from_json(j_student_1)
# print(new_student_1)
# print(type(new_student_1))
# print(
#     "{} {} {}".format(
#         new_student_1.first_name, new_student_1.last_name, new_student_1.age
#     )
# )
