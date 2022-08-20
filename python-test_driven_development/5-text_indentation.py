#!/usr/bin/python3
"""A module for spacing"""


def text_indentation(text):
    """Testing the function for idenation"""
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for c in text:
        line += c
        if c in ['.', '?', ':']:
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end="")
