#!/usr/bin/python3
"""Sript that takes your GitHub credentials
   (username and password) and uses the GitHub
   API to display your id
"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
