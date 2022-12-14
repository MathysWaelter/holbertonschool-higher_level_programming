#!/usr/bin/python3
"""
    function to create square
"""


class Rectangle:
    """
    Square:
        it's Rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        type(self).print_symbol

    def __str__(self):
        rect = ""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                rect += str(self.print_symbol)
            if i < self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """
        :param value:
            value of size for return current area
        """
        return self.width * self.height

    def perimeter(self):
        """
        :param value:
            value of size for return current perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @property
    def width(self):
        """
        :param value:
            value for define a square
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value:
            value for width of a square
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        :param value:
            value for define a square
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value:
            value for height of a square
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
