#!/usr/bin/python3
""""
This module contains and fefines a function that prints a given name
"""


def say_my_name(first_name, last_name=""):
    """This function prints name (<first name> <last name>)
    Args:
        first_name (str): The fisrt given name to be printed
        last_name (str): The last given name to be printed
    Raises:
        TypeError: If either the first_name and last_name are not strings
    """

    If not isinstance(First_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
