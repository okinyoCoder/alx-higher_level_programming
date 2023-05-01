#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
   displays the value of the X-Request-Id variable
   found in the header of the response
"""

from argv import sys
import urllib.request

if '__name__' == '__main__':
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print('{}'.format(page.X-Request-Id)):
