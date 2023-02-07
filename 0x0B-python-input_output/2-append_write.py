#!/usr/bin/python3
"""Module with a function that appends string to end of a file"""

def append_write(filename="", text=""):
    """function appends a string at the end of a text file"""

    with open(filename, 'a',  encoding="utf-8") as f:
        return f.write(text)
