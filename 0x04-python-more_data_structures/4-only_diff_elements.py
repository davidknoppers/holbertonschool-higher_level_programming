#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None:
        return (set_2)
    if set_2 is None:
        return (set_1)
    result = (set_1 | set_2) - (set_1 & set_2)
    return (result)
