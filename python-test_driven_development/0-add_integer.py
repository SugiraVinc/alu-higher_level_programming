#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    """
    Raising the type error message
    """
    if type(a) != type(int) and type(a) != type(float):
        raise TypeError(" a must be an integer ")
    if type(b) != type(int) and type(b) != type(float):
        raise TypeError(" b must be an integer ")
    if type(a, float):
        a = int(a)
    if type(b, float):
        b = int(b)
    return a+b
