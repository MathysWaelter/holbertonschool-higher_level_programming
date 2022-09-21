#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


from typing import Type
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def basic_test(self):
        self.assertEqual(max_integer([2, 9, 6, 1]), 9)

    def negative_test(self):
        self.assertEqual(max_integer([-9, -5, -11]), -5)

    def empty_test(self):
        self.assertEqual(max_integer(), None)

    def basic_negative_test(self):
        self.assertEqual(max_integer([2, -3, 5, -11, 666]), 666)

    def float_test(self):
        self.assertEqual(max_integer([4, 7, 3, 7.8]), 7.8)

    def char_test(self):
        with self.assertRaises(TypeError):
            max_integer([9, 6, 'r'])

if __name__ == '__main__':
    unittest.main()