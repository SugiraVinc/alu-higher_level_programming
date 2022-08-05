#!/usr/bin/python3
""" the sys module helps us to automatically assign arguments"""
import urllib.request
import sys


if __name__ == "__main__":
    """ Accessing the request"""

    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
