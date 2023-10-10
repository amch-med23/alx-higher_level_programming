#!/usr/bin/python3
""" this defines a python class to JSON fucntion """


def class_to_json(obj):
    """ returns the dictionary represantation of a simple data structure """
    return obj.__dict__
