#!/usr/bin/python3
"""
Basic module for file reading
Contains a basic read-file function
"""


def read_file(filename=""):
    """
    reads a file and prints it to stdout
    the with-open syntax autocloses the file
    including after an error!
    """
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
