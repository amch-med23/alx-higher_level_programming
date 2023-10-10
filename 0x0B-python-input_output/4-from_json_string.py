#!/usr/bin/python3
""" this model deserializes a json file into a text """
import json


def from_json_string(my_str):
    """ python object represantation of a JSON object """
    return json.loeads(my_str)
