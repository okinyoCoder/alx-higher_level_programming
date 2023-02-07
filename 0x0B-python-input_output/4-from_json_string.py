#!/usr/bin/python3
"""module has a function that returns an object Python data structure"""
 
from json import loads

def from_json_string(my_str):
    """function that returns an object (Python data structure)
     represented by a JSON string
    """
    return json.loads(my_str)
