#!/usr/bin/python3
"""new class Square inherit from Base.Rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """retrieve __init__ from Rectangle Class"""
        super(Square, self).__init__(size, size, x, y , id)
        self.size = size

    def __str__(self):
        """retrieve __str__ from Rectangle Class"""
        return super().__str__()
