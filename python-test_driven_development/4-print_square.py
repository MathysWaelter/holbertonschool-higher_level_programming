#!/usr/bin/python3
"""
    function to create square
"""


def print_square(size):
    """
    :param value:
        print square with #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for x in range(size):
            print()
            for space in range(size):
                 print("#", end="")
    elif size < 0:
        print()
        raise ValueError("size must be >= 0")
