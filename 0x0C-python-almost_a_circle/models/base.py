#!/usr/bin/python3
''' first class base '''
import json

class Base:
    ''' base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' class constructor '''
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None or list_dictionaries is == []:
            return  "{}"
        return json.dumps(list_dictionaries)
