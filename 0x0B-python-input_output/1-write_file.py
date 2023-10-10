#!/usr/bin/python3
""" this module defines a file writing fucntion """


def write_file(filename="", text=""):
    """ this function writes to a utf-8 file """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
