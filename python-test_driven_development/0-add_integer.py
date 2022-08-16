#!/usr/bin/python3
def add_integer(a, b=98):
    a = int(a)
    b = int(b)
    if type(a,b) not in (float, int):
        raise TypeError(" a must be an integer ")
    return a+b
