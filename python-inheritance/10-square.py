#!/usr/bin/python3
"""define a geometry print"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for print square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
