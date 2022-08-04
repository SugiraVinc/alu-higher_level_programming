#!/usr/bin/python3
"""Modules definition, here the sys module helps us to set parameters or argumentss"""
import urllib.request
import sys


""" Making our scripts executable """
if __name__ = "__main__":
    """ Using the sys module or library to provide url argument """
    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
