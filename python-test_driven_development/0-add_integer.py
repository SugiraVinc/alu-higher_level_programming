#!/usr/bin/python3
""" A function that adds two numbers """

""" Our function that helps to add numbers"""
def add_integer(a, b=98):
    try:
        if type(a) == int or float:
            sum = a+b
    except TypeError:
        print(" a must be an integer ")
    return sum
