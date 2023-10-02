#!/usr/bin/python3
""" A class that defines a rectangle """


class Rectangle:
    """ this defines the rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialization of the Rectangle class
        Args:
             width: represants the width of the rectangle
             height: represants the height of the rectangle
        Raises:
              TypeError: if the alue type of width and height is not integer
              ValueError: if the value is less than 0
"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    def height(self, value):
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

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ the daigram of the rectangle defined by the object """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for col in range(self.__height):
            for row in range(self.__width):
                try:
                    rec += str(self.print_symbol)
                except Exception:
                    rec += type(self).print_symbol
            if col < self.__height - 1:
                rec += "\n"
        return (rec)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ print the message for every object that is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() >= rect_1.area():
            return rect_2
        else:
            return rect_1
