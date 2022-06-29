#!/usr/bin/python3


"""This module adds 2 integers a and b

    The function add_integer returns int

    """


def add_integer(a: int, b=98) -> int:

    """Add two integers a and b

    Args:
        a - integer
        b - integer

    Return: int
    """

    if type(a) not in [int, float]:

        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:

        raise TypeError("b must be an integer")

    return int(a) + int(b)
