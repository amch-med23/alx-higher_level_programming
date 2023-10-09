#!/usr/bin/python3
"""
   this module returns a list of valid attributes
   and methods used by an object
"""


def lookup(obj):
    """ lookup for all the attributes and methods of an object """
    return dir(obj)
