#!/usr/bin/python3


"""
This module perform dot multiplication of 2 matrices \
    by using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """
    Dot multiplication of m_a and m_b using numpy
    Return:
        (Array)
    """

    return np.dot(m_a, m_b)
