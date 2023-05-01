#!/usr/bin/python3
"""Script that takes in a URL, sends a
   request to the URL and displays the body
   of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())
    except HTTPError as error:
        print("Error code: {}".format(error.code))
