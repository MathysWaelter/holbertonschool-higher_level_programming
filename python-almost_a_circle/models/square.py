#!/usr/bin/python3
"""new class Square inherit from Base.Rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """retrieve __init__ from Rectangle Class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """retrieve __str__ from Rectangle Class"""
        return("[Square] ({}) {}/{} - {}".format
               (self.id, self.x, self.y, self.size))
