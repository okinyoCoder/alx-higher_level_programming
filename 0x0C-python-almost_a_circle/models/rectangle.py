#!/usr/bin/python
'''  class Rectangle that inherits from Base '''

class Rectangle(Base):
    ''' class Rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructer '''
        super().__init __(self, id)
        self.not_integer('width', value)
        self.under_or_equal_zero('width', value)
        self.not_integer('height', value)
        self.under_or_equal_zero('height', value)
        self.under_zero('x', value)
        self.under_zero('y', value)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        ''' width getter function '''
        return self.__width

    @property
    def height(self):
        ''' height getter function '''
        return self.__height
    
    @property
    def x(self):
        ''' x getter function '''
        return self.__x

    @property
    def y(self):
        ''' y getter function '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' width setter function '''
        self.not_integer('width', value)
        self.under_or_equal_zero('width', value)
        return self.__width = value

    @height.setter
    def height(self, value):
        ''' height setter function '''
        self.not_integer('height', value)
        self.under_or_equal_zero('height', value)
        return self.__height = value

    @x.setter
    def x(self, value):
        ''' x setter function '''
        self.under_zero('x', value)
        return self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter function '''
        self.under_zero('y', value)
        return self.__y = value

    def not_integer(self, param = "", value):
        ''' function that checks if value is integer '''
        if not isinstance(value, int):
            raise TypeError("{param} must be an integer")

    def under_or_equal_zero(self, param = "", value):
        ''' function that checks if value is less than or equal to zero '''
        if value <= 0:
            raise ValueError("{param} must be > 0")

    def under_zero(self, param = "", value):
        ''' function that checks if value is under zero '''
        if value < 0:
            raise ValueError("{param} must be >= 0")

