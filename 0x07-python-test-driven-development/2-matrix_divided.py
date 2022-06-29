#!/usr/bin/python3

"""
This Module contains a function that divides all element of a matrix
"""


def matrix_divided(matrix, div):

    """
    Doc
    """
    errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(errormsg)
    for lst in matrix:
        for i in lst:
            if type(i) not in [int, float]:
                raise TypeError(errormsg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        raise TypeError(errormsg)

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    result = []
    for i in matrix:
        result.append(list(map(lambda n: round(n / div, 2), i)))

    return result
