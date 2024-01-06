#!/usr/bin/python3
"""
Implements a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: The peak element if found, otherwise None.
    """
    if not list_of_integers:
        return None

    l, h = 0, len(list_of_integers) - 1

    while l < h:
        m = (l + h) // 2

        if list_of_integers[m] > list_of_integers[m + 1]:
            h = m
        else:
            l = m + 1

    return list_of_integers[l]
