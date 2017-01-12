#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    best = None
    for key in my_dict.keys():
        if best is None or my_dict[key] > best:
            best = my_dict[key]
    return best
