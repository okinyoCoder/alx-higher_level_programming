#!/usr/bin/python3
""" module with class student """

class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """ class constant """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that retrieves dictionary repre of student """
        return self.__dict__
