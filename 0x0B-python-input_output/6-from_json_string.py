#!/usr/bin/python3
import json
"""
Module has one function
Demonstrates basic use of json objects
"""


def from_json_string(my_str):
    """
    take a string
    return its json representation

    """
    return(json.loads(my_str))
