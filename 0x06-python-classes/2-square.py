#!/usr/bin/python3
"""Using the square Class"""


class Square:
    """Initializing this class
    Args:
        size: represents the size of the defined square
    Raises:
          TypeError: error indication a type in not integer
          ValueError: error indicationg is the size is less than 0
    """
    def __int__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
