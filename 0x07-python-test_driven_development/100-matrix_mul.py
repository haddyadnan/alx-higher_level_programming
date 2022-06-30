#!/usr/bin/python3


"""
This module perform dot multiplication on 2 matrices
"""


def matrix_mul(m_a, m_b):

    """
    Multiply matrix m_a by matrix m_b
    Return:
        (list of list (ints)) m_a * m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")

    alen = 0
    for lst in m_a:
        for i in lst:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        alen += 1
    for lst in m_b:
        for i in lst:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only intergers or floats")

    idxa = len(m_a[0])
    idxb = len(m_b[0])

    blen = 0
    for lst in m_a:
        if len(lst) != idxa:
            raise TypeError("each row of m_a must be of the same size")
        # alen += 1
    for lst in m_b:
        if len(lst) != idxb:
            raise TypeError("each row of m_b must be of the same size")
        blen += 1

    # print(idxa, len(m_a))
    # print(idxb, len(m_b))
    # if len(m_a) != idxb:
    #     raise ValueError("m_a and m_b can't be multiplied")
    if idxa != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = [[sum(x * y for x, y in zip(r, c)) for c in zip(*m_b)] for r in m_a]

    return mul
