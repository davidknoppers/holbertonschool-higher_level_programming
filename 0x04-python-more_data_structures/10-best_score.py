#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    best = None
    best_key = None
    for key in my_dict.keys():
        if best is None or my_dict[key] > best:
            best = my_dict[key]
            best_key = key
    return best_key
