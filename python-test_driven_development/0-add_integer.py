#!/usr/bin/python3
""" A function that adds two numbers """


def add_integer(a, b=98):
    """ Raising the type error message"""
    try:
        if type(a) == int or float:
            sum = a+b
        if type(b) == int or float:
            sum = a+b
    except TypeError:
        print(" a must be an integer ")
    return sum
