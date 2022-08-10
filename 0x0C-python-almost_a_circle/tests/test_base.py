#!/usr/bin/python3

"""
Unittest for base
"""

import unittest

from models.base import Base

class TestBaseInit(unittest.TestCase):

    """
    Test Base Initialization
    """

    def test_auto_id(self):
        b1 = Base()
        self.assertEqual(1, b1.id)

    def test_auto_id_1(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id+1)

    def test_assign_id(self):
        b1 = Base(89)
        self.assertEqual(89, b1.id)

class TestBaseTJS(unittest.TestCase):

    """
    Test Base.to_json_string
    """

    def test_assign_none(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), '[]')
    
    def test_assign_lst(self):
        b = Base()
        self.assertEqual(b.to_json_string([]), '[]')

    def test_assign_val(self):
        b = Base()
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')

    def test_return_type(self):
        b = Base()
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')

    def test_wrong_input(self):
        #input takes 1 pos arg
        b = Base()
        with self.assertRaises(TypeError):
            b.to_json_string(2,3)
    
    def test_input_type(self):
        #input must iterable
        b = Base()
        with self.assertRaises(TypeError):
            b.to_json_string(2)

class testBaseFJS(unittest.TestCase):
    
    """
    test Base.from_json_string()
    """

    def test_assign_none(self):
        b = Base()
        self.assertEqual(b.from_json_string(None), [])

    def test_assign_empty(self):
        b = Base()
        self.assertEqual(b.from_json_string('[]'), [])
    
    def test_assign_value(self):
        b = Base()
        self.assertEqual(b.from_json_string('[{ "id": 10 }]'), [{ "id": 10 }])

    def test_input_type(self):
        b = Base()
        with self.assertRaises(TypeError):
            b.from_json_string([{ "id": 89 }])

    def test_return_type(self):
        b = Base()
        out = b.from_json_string('[{ "id": 10 }]')
        self.assertEqual(type(out), list)