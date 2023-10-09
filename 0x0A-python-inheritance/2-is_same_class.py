#!/user/bin/python3
"""
   Checks if object is an instance of the class, otherwise
   returns false
"""


def is_same_class(obj, a_class):
    """ Return true if object is an instance of the given calss, false
     Otherwise. """
    return (type(obj) == a_class)
