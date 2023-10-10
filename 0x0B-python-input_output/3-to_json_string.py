#!/usr/bin/python3
""" this module serialize a text to JSON """
import json


def to_json_string(my_obj):
    """ this serializes a string to JSON """
    return json.dumps(my_obj)
