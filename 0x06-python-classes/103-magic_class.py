#!/usr/bin/python3
""" creting the Magic Class """
import math


class MagicClass:

    def __init__(self, radius=0):
        """ initiation """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('raduis must be a number')
        self.__radius = radius

    def area(self):
        """ creating the area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ creating the circumference """
        return 2 * math.pi * self.__radius
