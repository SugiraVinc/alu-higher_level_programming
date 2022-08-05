#!/usr/bin/python3
""" Our modules """
import urllib.request
import sys

if __name__ == '__main__':
    req = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as e:
            print('Regular request')
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
