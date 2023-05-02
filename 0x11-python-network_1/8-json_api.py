#!/usr/bin/python3
"""Script that takes in a letter and sends a
   POST request to http://0.0.0.0:5000/search_user
   with the letter as a parameter
"""
from sys import argv
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) >= 2:
        value = argv[1]
    else:
        value = ''
    dataplay = {'q': value}
    r = requests.post(url, data=dataplay)
    try:
        json_file = r.json()
        if json_file:
            print("[{}] {}".format(
                json_file.get("id"), json_file.get("name")))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
