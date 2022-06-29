#!/usr/bin/python3

"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Check - Test Cases
    """

    def test_module_docstring(self):
        """test module docsting"""
        doc = __import__("6-max_integer").__doc__
        self.assertTrue(len(doc) > 1)

    def test_function_docstring(self):
        """test function docstring"""
        doc = max_integer.__doc__
        self.assertTrue(len(doc) > 1)

    def test_equal_4(self):
        """test equal 4"""
        test = [1, 2, 3, 4]
        self.assertEqual(max_integer(test), 4)

    def test_empty(self):
        """test empty"""
        test = []
        self.assertEqual(max_integer(test), None)

    def test_neg(self):
        """test var negative"""
        test = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test), -1)

    def test_single_var(self):
        """test 1 variable"""
        test = [1]
        self.assertEqual(max_integer(test), 1)

    def test_bool(self):
        """test bool"""
        test = [True, False, True]
        self.assertEqual(max_integer(test), True)

    def test_not_int(self):
        """test input not int"""
        test = ["str", "a"]
        with self.assertRaises(TypeError):
            max_integer(test)


if __name__ == "__main__":
    unittest.main()
