#!/usr/bin/python3
import urllib.request
import sys
""" the sys module helps us to automatically assign arguments from the libraries """

if __name__ = "__main__":
    """ Accessing the request"""

    req = sys.argv[1]
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
