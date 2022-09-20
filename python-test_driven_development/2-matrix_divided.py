#!/usr/bin/python3
"""function to print only two digit of divide"""


def custom_divid(a):
    """custom divid"""
    return float("%0.2f" % a)


"""function to print matrix divide"""


def matrix_divided(matrix, div):
    """divide matrix"""
    if (all([isinstance(item, int) for item in matrix])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float] or div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[custom_divid(item / div) for item in liste] for liste in matrix]
