#!/usr/bin/python3

"""
Modules has a functiuon that adds two numbers
"""

def add_integer(a, b=98):
    """ function that add two integer or float numbers
    Args:
        a:first number
        b:second number
    Returns:
        Addition of funtion arguements
    Raises:
        TypeError: 
             throws this if a or b are not integer of float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a+b)
