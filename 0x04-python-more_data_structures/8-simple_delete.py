#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    if my_dict is None:
        return None
    if key in my_dict.keys():
        del my_dict[key]
    return (my_dict)
