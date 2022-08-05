#!/usr/bin/python3
""" modules help to send a request and retrieve a header """
import requests
import sys


# url = 'https://intranet.hbtn.io'

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    dict_got = r.headers
    print(dict_got.get('X-Request-Id'))
