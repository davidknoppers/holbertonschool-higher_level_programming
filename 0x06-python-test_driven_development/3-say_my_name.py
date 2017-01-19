#!/usr/bin/python3
"""
say_my_name: Say my naaaame
Prints the name it's given unless your input is bad
Input must be two strings
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the two strings you pass it with a space between them
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
