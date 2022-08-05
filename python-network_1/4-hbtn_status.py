#!/usr/bin/python3
""" use request module to communicate with the server """
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    data = r.text
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
