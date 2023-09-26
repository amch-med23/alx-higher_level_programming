#!/usr/bin/python3
"""My square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"The propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
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
        """property of the coordinates of this Square
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or not a positive integer in tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """getting the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        p = ""
        if self.size == 0:
            return "\n"
        for j in range(self.position[1]):
            p += "\n"
        for j in range(self.size):
            for x in range(self.position[0]):
                p += " "
            for z in range(self.size):
                p += "#"
            p += "\n"
        return p

    def my_print(self):
        """print the square in the given position"""
        print(self.pos_print(), end='')
