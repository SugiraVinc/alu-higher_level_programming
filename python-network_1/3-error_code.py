#!/usr/bin/python3
""" Our modules """
import urllib.request
import sys

if __name__ == '__main__':
    req = sys.argv[1]
    data = sys.argv[2]
    data = data.encode('utf-8')
    try:
        with urllib.request.urlopen(req) as e:
            print('Our request')
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
