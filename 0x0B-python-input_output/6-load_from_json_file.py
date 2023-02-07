#!/usr/bin/python3
""" object from aJSON file """

import json

def load_from_json_file(filename):
    """ creates an Object from a JSON file """

     with open(filename) as f_bj:
         return json.load(f_bj)
