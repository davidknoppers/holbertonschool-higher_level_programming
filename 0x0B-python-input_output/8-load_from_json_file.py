#!/usr/bin/python3
import json
"""
One function in this module
load_from_json_file does what you would expect
"""


def load_from_json_file(filename):
    """
    open file
    load json object
    return that object
    """
    with open(filename, mode='r') as myFile:
        return json.load(myFile)
