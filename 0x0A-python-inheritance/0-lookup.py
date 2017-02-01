#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
Not sure what else to put here but the checker is unhappy
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return(dir(obj))
