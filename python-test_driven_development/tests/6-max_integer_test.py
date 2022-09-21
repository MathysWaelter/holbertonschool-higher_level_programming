#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def basic_test(self):
        self.assertEqual(max_integer([2, 9, 1]), 9)
        self.assertEqual(max_integer([-5, -9, -11]), -5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 3, 5, -11, 666]), 666)
        self.assertEqual(max_integer([4, 7, 3, 7.8]), 7.8)
        self.assertEqual(max_integer([8]), 8)