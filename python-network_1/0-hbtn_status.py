#!/usr/bin/python3
''' We are not importing any module other than urllib request'''
import urllib.request


'''We have to use with to fetch the url'''
req = urllib.request.Request('https://intranet.hbtn.io/status')
'''Let us create a variable'''
with urllib.request.urlopen(req) as response:
    '''Printing the body of our fetch'''
    print(+str(req.getcode()))
'''We can now run it'''
