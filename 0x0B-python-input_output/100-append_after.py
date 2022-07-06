#!/usr/bin/python3

"""
This module appends a string at the end of a text file (UTF8)
and returms number of characters added
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert new_string after every occurence of new string
    """

    with open(filename, "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
        f.seek(0)
        f.write("".join(lines))
