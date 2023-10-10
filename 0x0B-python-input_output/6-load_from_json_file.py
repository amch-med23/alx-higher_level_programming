#!/usr/bin/python3
""" this module is loading json file content """
import json


def load_from_json_file(filename):
    """ creates aobject from a json """
    with open(filename) as f:
        return json.load(f)
