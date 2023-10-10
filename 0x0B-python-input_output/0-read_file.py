#!/usr/bin/python3
""" this is a module to read and print the content of a file """

def read_file(filename=""):
    """ this function reads and outputs a content of a text file """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')

