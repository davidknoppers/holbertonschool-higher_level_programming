#!/usr/bin/python3
def complex_delete(my_dict, value):
    if my_dict is None:
        return None
    keys_to_delete = []
    for key in my_dict.keys():
        if my_dict[key] == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del my_dict[key]
    return my_dict
