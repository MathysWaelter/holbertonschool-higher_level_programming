#!/usr/bin/python3
"""function to define if obj == a_class"""


def is_same_class(obj, a_class):
    """define true of false"""
    if type(obj) == a_class:
        return True
    else:
        return False
