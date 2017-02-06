#!/usr/bin/python3
"""
module contains one function
append_after takes advantage of python's awesome string capabilities
adds a string to any line in a file that contains a search string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    open a file
    go through it line by line and update strings
    return to beginning of file and rewrite it
    """
    result = ""
    with open(filename, mode='r+', encoding='utf-8') as MyFile:
        for line in MyFile:
            if search_string in line:
                result += line + new_string
            else:
                result += line
        MyFile.seek(0)
        MyFile.write(result)
