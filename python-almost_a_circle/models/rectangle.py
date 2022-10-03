#!/usr/bin/python3
"""define a new class rectangle inherits form Base"""


from models.base import Base


class Rectangle(Base):
    """Class inherits from SuperClass"""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = Rectangle.__nb_objects
        

    @property
    def width(self):
        """
        :param value:
            value for define a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        :param value:
            value for width of a rectangle
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
            value for define a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        :param value:
            value for height of a rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """
        :param value:
            value for define a rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        :param value:
            value for x of a rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        :param value:
            value for define a rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        :param value:
            value for x of a rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__y = value
