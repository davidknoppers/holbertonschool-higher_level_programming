#!/usr/bin/python3
"""
Add_integer: adds two ints and returns their result
Inputs a and b must be integers
Floats are converted to ints before addition occurs
"""


def add_integer(a, b):
    """
    Adds two ints and returns their result. Error-handled.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
