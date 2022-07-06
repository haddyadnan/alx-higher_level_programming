#!/usr/bin/python3

"""
This module writes a string to a text file (UTF8)
and returms number of characters written
"""


def write_file(filename="", text=""):

    """
    write text to filename
    """

    with open(filename, "w") as f:
        return f.write(text)
