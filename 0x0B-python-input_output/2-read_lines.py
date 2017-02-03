#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        count = 0
        if nb_lines <= 0:
            print(myFile.read())
        else:
            for line in myFile:
                if count < nb_lines:
                    print(line)
                    count += 1
                else:
                    break
