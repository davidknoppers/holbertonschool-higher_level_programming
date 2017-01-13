#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: " + str(error) + "\n")
        return None
