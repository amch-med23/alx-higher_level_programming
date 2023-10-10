#!/usr/bin/python3
""" this module defines a text appending function """


def append_write(filename="", text=""):
    """ this appends a text to a text file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
