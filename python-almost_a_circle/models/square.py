#!/usr/bin/python3
"""new class Square inherit from Base.Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """retrieve __init__ from Rectangle Class"""
        super().__init__(size, size, x, y, id)

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
               (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assign all args"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
