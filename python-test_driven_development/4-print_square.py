#!/usr/bin/python3
"""A module to build a square"""

def print_square(size):
    """A function to display the square"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for i in range(size):
            print("#" * size)
