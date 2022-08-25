#!/usr/bin/python3

"""A module to help with IDs"""
import json
import csv
# import turtoo library function
from random import choice as random


class Base:
    """A simple class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
