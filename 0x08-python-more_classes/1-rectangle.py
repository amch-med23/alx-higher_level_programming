#!/usr/bin/python3
""" A class that defines a rectangle"""


class Rectangle:
    """ this defines the rectangle """

    def __init__(self, width=0, height=0):
        """initialization of the Rectangle class
        Args:
             width: represants the width of the rectangle
             height: represants the height of the rectangle
        Raises:
              TypeError: if size is not integer
              ValueError: if size is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retreives the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retreives the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
