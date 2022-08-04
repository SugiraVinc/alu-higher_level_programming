#!/usr/bin/python3
""" module uses another module to request to make request """
import urllib.request


    """making request to provided url"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        """ Decoding our content """
        temp = str(html)
        print("\t- utf8 content: {}".format(temp[2:-1]))
