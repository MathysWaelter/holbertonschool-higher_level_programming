#!/usr/bin/python3
"""
    function to create square
"""


class Square():
    """
    Square:
        it's square
        :param value:
        value of size
    """

    def __init__(self, size=0, message=""):
        """
        :param value:
            value of size and message for raise
        """
        self.__size = size

    def area(self):
        """
        :param value:
            value of size for return current area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        :param value:
            print square with #
        """
        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print()

    @property
    def size(self):
        """
        :param value:
            value for define a square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise NameError("size must be >= 0")
        self.__size = value