#!/usr/bin/python3
"""
Only one function here
write_file writes to a basic file
"""


def write_file(filename="", text=""):
    """
    open the file
    write to it
    return number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        chars_written = myFile.write(text)
    return chars_written
