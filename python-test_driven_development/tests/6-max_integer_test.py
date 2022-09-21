#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 8, 6]), 8)
        self.assertEqual(max_integer([10, 2, 8, 6]), 10)
        self.assertEqual(max_integer([4, 2, -8, 6]), 6)
        self.assertEqual(max_integer([-4, -2, -8, -6]), -2)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)