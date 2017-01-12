#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    best = 0
    for key in my_dict.keys():
        if my_dict[key] > best:
            best = my_dict[key]
    return best
