#!/usr/bin/python3
"""The square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A module that draws from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Using super class instant method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String formatting"""
        m = self.id
        w = self.height
        l = self.x
        o = self.y
        return ("[Square] ({}) {}/{} - {}".format(m, w, l, b))

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, b):
        """set size function"""
        if type(b) is not int:
            raise TypeError("width must be an integer")
        if b <= 0:
            raise ValueError("width must be > 0")
        self.width = b
        self.height = b

        # Methods
    def update(self, *args, **kwargs):
        """Let's update our square methods
        """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for i in range(len(args) if len(args) <= 4 else 4):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, b in dct.items():
                if key == 'id' and b is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, b)

    def to_dictionary(self):
        """
        Dictionary representation of data
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
