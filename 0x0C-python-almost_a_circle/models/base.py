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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''
        filename = cls.__name__ + ".json"

        with open("filename", "w") as f:
            if list_objs is None:
                f.write("[]")

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        '''' function thatreturns the list of the JSON string representation json_string '''
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)
