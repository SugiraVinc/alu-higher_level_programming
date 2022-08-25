#!/usr/bin/python3
"""A rectangular module"""
from models.base import Base


class Rectangle(Base):
    """The class to help us"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class intance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, d):
        """Width setter"""
        if type(d) != int:
            raise TypeError("width must be an integer")
        if d <= 0:
            raise ValueError("width must be > 0")
        self.__width = d

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, z):
        """set height"""
        if type(z) != int:
            raise TypeError("height must be an integer")
        if z <= 0:
            raise ValueError("height must be > 0")
        self.__height = z

    @property
    def x(self):
        """set x"""
        return self.__x

    @x.setter
    def x(self, a):
        """set x"""
        if type(a) != int:
            raise TypeError("x must be an integer")
        if a < 0:
            raise ValueError("x must be >= 0")
        self.__x = a

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, b):
        """Setter y"""
        if type(b) != int:
            raise TypeError("y must be an integer")
        if b < 0:
            raise ValueError("y must be >= 0")
        self.__y = b

    def area(self):
        """Calculating the Area"""
        return (self.__height * self.__width)

    def display(self):
        """Display our output"""
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """String showcase of our arguments"""
        o = self.id
        p = self.__x
        r = self.__y
        s = self.__width
        t = self.__height
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(o, p, r, s, t))

    def update(self, *args, **kwargs):
        """take multi update"""
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args) if len(args) <= 5 else 5):
                    dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == "id" and d is None:
                    p = self.__width
                    r = self.__height
                    s = self.__x
                    self.__init__(p, r, s, self.__y)
                else:
                    setattr(self, key, d)

    def to_dictionary(self):
            """dictionary formatting"""
            dict = {}
            dict["id"] = self.id
            dict["width"] = self.width
            dict["height"] = self.height
            dict["x"] = self.x
            dict["y"] = self.y
            return (dict)
