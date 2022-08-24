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

    # getter method for width
    def get_width(self):
        """width getter"""
        return self.__width

    # setter method for width
    def set_width(self, d):
        """Width setter"""
        self.__width = d

    # getter method for height
    def get_height(self):
        """get height"""
        return self.__height

    # setter method for height
    def set_height(self, z):
        """set height"""
        self.__height = z

    # x getter method
    def get_x(self):
        """set x"""
        return self.__x

    # x setter
    def set_x(self, a):
        """set x"""
        self.__x = a
    
    # y getter
    def get_y(self):
        """y getter"""
        return self.__y
    
    # y setter
    def set_y(self, b):
        """Setter y"""
        self.__y = b
