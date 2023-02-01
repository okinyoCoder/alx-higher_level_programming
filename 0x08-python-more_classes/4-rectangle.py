#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and heigh
    """

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ return area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.height == 0 or self.width == 0:
            return ''
        new_str = ''
        for col in range(self.height):
            for row in range(self.width):
                new_str += '#'
        return new_str

        return self.__draw_rectangle()

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """
        w = str(eval('self.width'))
        h = str(eval('self.height'))
        return 'Rectangle({}, {})'.format(w, h)
