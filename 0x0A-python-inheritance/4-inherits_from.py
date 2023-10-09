#!/usr/bin/python3
"""
   Checks if the object of a class is inheritance of a class
   or an instance of it.
"""


def inherits_from(obj, a_class):
    """ true if the object is an instance of the class, false otherwise """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
