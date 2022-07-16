#!/usr/bin/python3

"""
test cases for Square class
"""

import unittest

from models.square import Square
from models.rectangle import Rectangle

from models.base import Base


class testSquareInit(unittest.TestCase):

    """
    Test Square Init
    """

    def test_no_value(self):
        with self.assertRaises(TypeError):
            Square()
    
    def test_one_value(self):
        self.assertIsInstance(Square(1,2), Base)

    
    def test_two_values(self):
        self.assertIsInstance(Square(1,2), Base)

    def test_three_values(self):
        self.assertIsInstance(Square(1,2,3), Base)

    def test_four_values(self):
        self.assertIsInstance(Square(1,2,3,4), Base)

    def test_five_values(self):
        with self.assertRaises(TypeError):
            Square(1,2,3,4,5)

    def test_input_type1(self):
        with self.assertRaises(TypeError):
            Square("1",2,3,4,5)
    
    def test_input_type2(self):
        with self.assertRaises(TypeError):
            Square(1,"2",3,4,5)
    
    def test_input_type3(self):
        with self.assertRaises(TypeError):
            Square(1,2,"3",4)

    def test_size_range(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_sizeis_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_xrange(self):
        with self.assertRaises(ValueError):
            Square(1,2,-3,4)
    
    def yrange(self):
        with self.assertRaises(ValueError):
            Square(1,2,3,-4)