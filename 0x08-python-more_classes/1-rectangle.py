#!/usr/bin/python3
"""
A module with a Rectangle

"""


class Rectangle:
    """
    parameters
    ----------
    """
    def __init__(self, width=0, height=0):
        """
        parameters
        ----------
        width : int
             the width of rectangle
        height : int
             width of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        a getter method that return rectangle width
        """
        return self.width

    @width.setter
    def width(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            value (int): The width of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) !=  int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

     @property
    def height(self):
        """
        a getter method that return rectangle height
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Checks the parameters and set the size of the Rectangle
        Args:
            value (int): height of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
        """
        if type(value) !=  int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value
