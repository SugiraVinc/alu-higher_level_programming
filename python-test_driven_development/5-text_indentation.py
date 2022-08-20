#!/usr/bin/python3
"""A module for spacing"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    print(".", end="")
    print("" + '\n')
    print("" + '\n')
    print("?", end="")
    print("" + '\n')
    print("" + '\n')
    print(":")
    print("" + '\n')
    print("" + '\n')
