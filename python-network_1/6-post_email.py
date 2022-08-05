#!/usr/bin/python3
""" Posting to a link """
import sys
import requests


if __name__ == "__main__":
    # create dictionary of data to post
    res = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(res.text)
