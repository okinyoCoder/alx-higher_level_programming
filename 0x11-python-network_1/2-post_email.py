#!/usr/bin/python3
"""script that takes in a URL and an email sends a POST
   request to the passed URL with the email as a parameter
   and displays the body of the response (decoded in utf-8)
"""
from argv import sys
import urllib.request

if '__name__' == '__main__':
    data = argv[2]
    data = data.encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.openurl(req) as response:
        result = response.read()
        print('Your email is: {}'.format(result.))
