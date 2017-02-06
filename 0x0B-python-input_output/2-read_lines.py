#!/usr/bin/python3
"""
Module contains one function
read_lines opens files and reads nb_lines lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Open file
    Read nb_lines
    Close file
    """
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        count = 0
        if nb_lines <= 0:
            print(myFile.read(), end="")
        else:
            nb_lines = int(nb_lines)
            for line in myFile:
                if count < nb_lines:
                    print(line, end="")
                    count += 1
                else:
                    break
