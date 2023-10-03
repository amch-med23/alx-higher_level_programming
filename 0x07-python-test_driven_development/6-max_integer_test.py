#!/usr/bin/python3
"""
This module contains and defines  a function
to find the max integer in a given list
"""


def max_integer(list=[]):
    """
        Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    res = list[0]
    x = 1
    while x < len(list):
        if list[x] > res:
            res = list[x]
        x += 1
    return res
