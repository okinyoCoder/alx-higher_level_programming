#!/usr/bin/python3
"""Model with a function that reads a text file"""

def read_file(filename=""):
    """Function that reads a text file and prints it to stdout
       Args:
           Filename: file that should be read
       Return: returns nothing
    """
    with open('filename', encoding = "utf-8") as f:
        print(f.read(), end = "")
