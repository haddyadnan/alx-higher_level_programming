#!/usr/bin/python3

"""
test cases for Rectangle class
"""

import unittest

from models.rectangle import Rectangle
from models.base import Base


class testRectangleInit(unittest.TestCase):

    """
    Test Rectangle Init
    """

    def test_no_value(self):
        with self.assertRaises(TypeError):
            Rectangle()
    
    def test_one_value(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
    
    def test_two_values(self):
        self.assertIsInstance(Rectangle(1,2), Base)

    def test_three_values(self):
        self.assertIsInstance(Rectangle(1,2,3), Base)

    def test_four_values(self):
        self.assertIsInstance(Rectangle(1,2,3,4), Base)

    def test_five_values(self):
        self.assertIsInstance(Rectangle(1,2,3,4,5), Base)

    def test_six_values(self):
        with self.assertRaises(TypeError):
            Rectangle(1,2,3,4,5,6)
    
    def test_input_type1(self):
        with self.assertRaises(TypeError):
            Rectangle("1",2,3,4,5)
    
    def test_input_type2(self):
        with self.assertRaises(TypeError):
            Rectangle(1,"2",3,4,5)
    
    def test_input_type3(self):
        with self.assertRaises(TypeError):
            Rectangle(1,2,"3",4,5)
    
    def test_input_type4(self):
        with self.assertRaises(TypeError):
            Rectangle(1,2,3,"4",5)

    def test_height_range(self):
        with self.assertRaises(ValueError):
            Rectangle(-1,2)
    
    def test_weight_range(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
    
    def test_weightis_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_heightis_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_xrange(self):
        with self.assertRaises(ValueError):
            Rectangle(1,2,-3,4)
    
    def yrange(self):
        with self.assertRaises(ValueError):
            Rectangle(1,2,3,-4)