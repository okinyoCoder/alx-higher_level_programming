#!/usr/bin/python

from models.base import Base

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

    def area(self):
        ''' returns the area value of the Rectangle '''
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__():
        ''' function that prints content of a rectangle '''
        return "[Rectangle] (<>) <>/<> - <>/<>".format(self.id, 
                                                       self.x, self.y, 
                                                       self.width, self.height)

    def update(self, *args):
        ''' update rectangle function '''
        if len(args) != 0:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        else:
            self.__init__(self.width, self.height, self.x, self.y)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
