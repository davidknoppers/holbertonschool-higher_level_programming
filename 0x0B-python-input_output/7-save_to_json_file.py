#!/usr/bin/python3
import json
"""
module contains just one function
save_to_json_file opens a file and writes a json object to it
"""


def save_to_json_file(my_obj, filename):
    """
    open file
    write json object to it
    close file
    """
    with open(filename, mode="w+") as myFile:
        myFile.write(json.dumps(my_obj))
