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
        self.__width = d

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, z):
        """set height"""
        self.__height = z

    @property
    def x(self):
        """set x"""
        return self.__x

    @x.setter
    def x(self, a):
        """set x"""
        self.__x = a

    @property
    def y(self):
        """y getter"""
        return self.__y 

    @y.setter
    def y(self, b):
        """Setter y"""
        self.__y = b
