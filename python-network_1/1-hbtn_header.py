#!/usr/bin/python3
import urllib.request
import sys
"""We use sys to add arguments"""

""" Providing url"""
if __name__ = "__main__":
    """ Using the sys module or library to provide url argument """

    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
