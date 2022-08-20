#!/usr/bin/python3
"""A module for spacing"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    print(".", end="")
    print()
    print()
    print("?", end="")
    print()
    print()
    print(":")
    print()
    print()
