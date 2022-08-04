#!/usr/bin/python3
''' We are not importing any module other than urllib request'''


import urllib.request
'''We have to use with to fetch the url'''
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
