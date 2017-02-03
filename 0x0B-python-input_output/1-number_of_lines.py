#!/usr/bin/python3
def number_of_lines(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        count = 0
        for line in myFile:
            count += 1
        return(count)
