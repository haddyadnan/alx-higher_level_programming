#!/usr/bin/python3

"""
This module reads a textfile and print to stdout
"""


def read_file(filename=""):

    """
    reads filename and prints to stdout
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
