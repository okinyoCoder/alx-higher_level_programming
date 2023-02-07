#!/usr/bin/python3
"""Model with a function that reads a text file"""

def read_file(filename=""):
    """Function that reads a text file and prints it"""

    with open(filename, 'r', encoding = "utf-8") as f:
        words = f.read()
        print(words, end="")
