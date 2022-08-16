#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    """
    Raising the type error message
    """
    if not isinstance(a) != int or float:
        raise TypeError(" a must be an integer ")
    if not isinstance(b) != int or float:
        raise TypeError(" b must be an integer ")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a+b
