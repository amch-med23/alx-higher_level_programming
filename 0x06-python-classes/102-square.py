#!/usr/bin/python3
""" the Square module """


class Square:
    """ definig the class """

    def __init__(self, size=0):
        """ creating the square
        Args:
        size: the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ the property of size of the square
        Raises:
              TypeError: if size is not an integer
              ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        getting the rea of a square
        Return: returns the size of the square
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __eq__(self, other):
        return self.area() == other.area()
