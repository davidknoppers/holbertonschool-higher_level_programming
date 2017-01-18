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
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
