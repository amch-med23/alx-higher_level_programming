#!/usr/bin/python3

"""defining the square size"""


class Square:
    """ the Square class """
    def __init__(self, size=0):
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

    def __str__(self):
        self.my_print()

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ Set a position of this square
        Args:
            value: as a tuple of two numbers
        Raises:
              TypeError: if the value is not two positive values
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculates the area of the defined square
        Return: the area of the square
        """
        return (self.__size ** 2)

    def pos_print(self):
        """
        returns the position of the square in the spaces
        """
        p = ""
        if self.__size == 0:
            return "\n"
        for j in range(self.position[1]):
            p += "\n"
        for j in range(self.size):
            for y in range(self.position[0]):
                p += " "
            for z in range(self.size):
                p += "#"
            p += "\n"
        return (p)

    def my_print(self):
        """ prints the square in the given position"""
        print(self.pos_print(), end='')
