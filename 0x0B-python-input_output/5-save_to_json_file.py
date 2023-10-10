#!/usr/bin/python3
""" this model saves an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ this saves the object to a text file """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
