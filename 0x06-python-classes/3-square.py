#!/usr/bin/python3

"""the Square Class"""


class Square:
    """this square has a private instance attribute called size"""

    def __init__(self, size=0):
        """
        initialization
        Args:
            size: the size of the defined square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
            calculates the  area of the defined square
            Returns:
                   the area of the defined square
        """
        return self.__size ** 2
