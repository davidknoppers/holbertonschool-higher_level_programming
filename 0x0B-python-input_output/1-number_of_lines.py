#!/usr/bin/python3
"""
Module containing just one function
number_of_lines merely returns a linecount
"""


def number_of_lines(filename=""):
    """
    Open file
    Count its lines
    Close the file
    """
    count = 0
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        for line in myFile:
            count += 1
    return(count)
