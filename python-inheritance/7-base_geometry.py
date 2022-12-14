#!/usr/bin/python3
"""define a geometry print"""


class BaseGeometry:
    """Class for print a bass geometry"""

    def area(self):
        """method for return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for check type of variable"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
