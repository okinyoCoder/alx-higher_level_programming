#!/usr/bin/python3
"""script that takes in a Url and sends
   request to the URL and displays the value of
   the variable X-Request-Id in the response header
"""
from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
