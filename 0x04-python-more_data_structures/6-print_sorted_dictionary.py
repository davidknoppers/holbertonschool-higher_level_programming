#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict is None:
        return (None)
    for key, val in sorted(my_dict.items()):
        print("{}: {}".format(key, val))
