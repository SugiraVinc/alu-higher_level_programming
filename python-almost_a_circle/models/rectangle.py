#!/usr/bin/python3
"""A rectangular module"""
from base import Base


class Rectangle(Base):
    """The class to help us"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class intance"""
        Base.__init__(id)
        self.width = width
        self.height =height
        self.x = x
        self.y = y
