#!/usr/bin/python3
"""define a new class rectangle inherits form Base"""


from symbol import argument
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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """function for return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """function for display rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__y):
            print("")
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end='')
            if i < self.__height - 1:
                print()
        print()

    def __str__(self):
        """function for display size of rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format
               (self.id, self.__x, self.__y, self.__width, self.__height))

    def define_update(self, id=None, width=None, height=None, x=None, y=None):
        """args assignment"""
        if id is not None:
            self.id == id
        if width is not None:
            self.width == width
        if height is not None:
            self.height == height
        if x is not None:
            self.x == x
        if y is not None:
            self.y == y

    def update(self, *args):
        """assign an argument to each attribute with define_update function"""
        if args:
            self.define_update(*args)

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
