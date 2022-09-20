#!/usr/bin/python3
"""function to add"""


def add_integer(a, b=98):
    """function to add two digit"""

    if type(a) not in [int, float] or a != a:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b != b:
        raise TypeError("b must be an integer")
    else:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)

    return a + b
