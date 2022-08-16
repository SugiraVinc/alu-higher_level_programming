#!/usr/bin/python3
""" A function that adds two numbers """


def add_integer(a, b=98):
    """ Raising the type error message"""
    try:
        if type(a) == int or float:
            sum = a+b
        if type(b) == int or float:
            sum = a+b
        else:
            raise TypeError(" b must be an integer")
    except TypeError:
        print(" b must be an integer ")
    return int(a) + int(b)
