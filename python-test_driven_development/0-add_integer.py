#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    """
    Raising the type error message
    """
    if not type(a, int) or not type(a, float):
        raise TypeError(" a must be an integer ")
    if not type(b, int) or not type(b, float):
        raise TypeError(" b must be an integer ")
    return a+b
