#!/usr/bin/python3


"""
This module contains a function that prints a square with the character #
"""


def print_square(size):

    """
    Print square using arg size
    Return:
        (string) size x size matrix
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    char = "#"
    char *= size
    for i in range(size):
        print(char)
