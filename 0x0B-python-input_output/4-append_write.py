#!/usr/bin/python3
"""
One function in this module
append_write opens a file and appends some text to it
"""


def append_write(filename="", text=""):
    """
    open file
    put some text at the end of it
    close that file
    """
    with open(filename, mode='a', encoding="utf-8") as myFile:
        chars_written = myFile.write(text)
    return chars_written
