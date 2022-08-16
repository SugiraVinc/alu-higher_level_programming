#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    """
    Raising the type error message
    """
    if not type(a) == int or float:
        raise TypeError(" a must be an integer ")
    if not type(b) == int or float:
        raise TypeError(" b must be an integer ")
    return a+b
