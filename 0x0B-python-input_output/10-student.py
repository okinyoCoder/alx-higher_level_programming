#!/usr/bin/python3
""" module with class student """

class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """ class constant """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method that retrieves dictionary repre of student """

        class_d = self.__dict__
        sel_d = dict()

        if isinstance(attrs, list):
            for attr in attrs:
                if not isinstance(attr, str):
                    return class_d

                if attr in class_d:
                    sel_d[attr] = class_d[attr]

            return sel_d

        return class_d
