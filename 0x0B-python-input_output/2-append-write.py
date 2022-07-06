#!/usr/bin/python3

"""
This module appends a string at the end of a text file (UTF8)
and returms number of characters added
"""


def append_write(filename="", text=""):

    """
    apppend text to filename
    """

    with open(filename, "a") as f:
        return f.write(text)
