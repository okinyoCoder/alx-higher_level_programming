#!/usr/bin/python3
"""Module that prints square with the character #"""

def print_square(size):
    """function that prints square

    Args:
        size: length of the square
    Return:
        returns nothing
    Raise:
        typeError: if size not an integer
                   if size if float and less than 0
        valueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size ,0 or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
