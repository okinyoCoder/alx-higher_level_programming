#!/usr/bin/python3
"""Module containing a function that has  writes a 
string to a text file
"""

def write_file(filename="", text=""):
    """ function at writes a string to a text file (UTF8) 
    and returns the number of characters written
    """

    with open(filename, 'w',  encoding="utf-8") as f:
        return f.write(text)

