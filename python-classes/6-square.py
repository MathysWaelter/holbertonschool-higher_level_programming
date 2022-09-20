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

    def __init__(self, size=0, position=(0, 0)):
        """
        :param value:
            value of size and message for raise
        """
        self.__size = size
        self.position = position

    def area(self):
        """
        :param value:
            value of size for return current area
        """
        return self.__size * self.__size

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

    @property
    def position(self):
        """
        to retrieve position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        to set position
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        :param value:
            print square with #
        """
        if self.__size > 0:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for space in range(self.__size):
                    print("#", end="")
                print()
        elif self.__size == 0:
            print()
