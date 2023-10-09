#!/usr/bin/python3
"""
   Defines a base geometry class BaseGeometry
"""


class BaseGeometry:
    """ represants a base geometry """

    def area(self):
        """ this arae in not implemented """
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """ validate the value of an integer """
        if type(value) != int:
            raise TypeError("{} is not an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
