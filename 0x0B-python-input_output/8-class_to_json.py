#!/usr/bin/python3
''' returns the dictionary description with simple data structure
'''

def class_to_json(obj):
     """ retuns the dictionary description with simple data structure """
     dictionary ={}
     dictionary = obj.__dict__.copy()
     return dictionary
