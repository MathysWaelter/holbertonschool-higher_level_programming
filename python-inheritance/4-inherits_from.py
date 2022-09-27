#!/usr/bin/python3
"""function that returns True if the object is an inheritable"""


def inherits_from(obj, a_class):
    """define true of false"""
    if type(obj) == a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
