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
        if d is not int:
            raise TypeError("width must be an integer")
        elif d <= 0:
            raise ValueError("width must be >0")
        else:
            self.__width = d

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, z):
        """set height"""
        if z is not int:
            raise TypeError("height must be an integer")
        elif z <= 0:
            raise ValueError("width must be >0")
        else:
            self.__height = z

    @property
    def x(self):
        """set x"""
        return self.__x

    @x.setter
    def x(self, a):
        """set x"""
        if a is not int:
            raise TypeError("height must be an integer")
        elif a <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = a

    @property
    def y(self):
        """y getter"""
        return self.__y 

    @y.setter
    def y(self, b):
        """Setter y"""
        if b is not int:
            raise TypeError("height must be an integer")
        elif b <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = b
