#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = printed = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
            i += 1
        except (TypeError, ValueError):
            i += 1
            continue
    print("")
    return printed
