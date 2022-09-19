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

    def __init__(self, __size=0, message=""):
        """
        :param value:
            value of size and message for raise
        """

        if not isinstance(__size, int):
            raise TypeError("size must be an integer".format(message))
        if __size < 0:
            raise NameError("size must be >= 0".format(message))
        self.__size = __size

    def area(self):
        """
        :param value:
            value of size for return current area
        """
        return self.__size * self.__size