#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    """
    Raising the type error message
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError(" a must be an integer ")
    if not isinstance(b, int):
        raise TypeError(" b must be an integer ")
    if isinstance(a, int) and isinstance(b, int):
        sum = a+b
    return sum
