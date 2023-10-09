#!/usr/bin/python3
"""
   Checksif the object is an instance of a class or
   an inherited class
"""


def is_kind_of_class(obj, a_class):
    """ returns true if the object is an instance of the class
        , and false if it was an inheritance from it
    """
    return (isinstance(obj, a_class))
