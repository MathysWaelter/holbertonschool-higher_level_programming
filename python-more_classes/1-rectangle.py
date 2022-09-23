#!/usr/bin/python3
"""
    function to create square
"""


class Rectangle:
    """
    Square:
        it's Rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def __width(self):
        """
        :param value:
            value for define a square
        """
        return self.__width

    @__width.setter
    def __width(self, value):
        """
        :param value:
            value for width of a square
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def __height(self):
        """
        :param value:
            value for define a square
        """
        return self.__height

    @__height.setter
    def __height(self, value):
        """
        :param value:
            value for height of a square
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
