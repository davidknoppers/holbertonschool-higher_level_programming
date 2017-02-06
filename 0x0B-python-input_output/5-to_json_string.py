#!/usr/bin/python3
import json
"""
module contains one function
to_json_string demonstrates basics of using json files
"""


def to_json_string(my_obj):
    """
    imports json
    'dumps' stands for 'dump string'
    returns string rep of a json object
    """
    return(json.dumps(my_obj))
