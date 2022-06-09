#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    squares = []
    for i in matrix:
        squares.append(list(map(lambda i: i**2)))
    return squares
