#!/usr/bin/python3

"""defining the square size"""

class Square:
    """ the Square class """
    def __int__(self, size=0):
        """ Initiating the square """
        """
        Args:
            size: the square size
        Raises:
              TypeError: the type error
              ValueError: the value error
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    @property
    def size(self):
        """
        retrieves the size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the defined square
        Return: the area of the square
        """
        return (self.__size ** 2)
