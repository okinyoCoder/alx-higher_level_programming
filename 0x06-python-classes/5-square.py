#!/usr/bin/python3
""" A class Square that defines a square by:
    Private instance attribute: size
    Public instance method: def area(self)
"""


class Square:
    """class constructor"""
    def __init__(self, size = 0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns  area of a square"""
        return self.__size ** 2

    """size getter"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print()
