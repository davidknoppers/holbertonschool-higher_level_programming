#!/usr/bin/python3
def new_in_list(list, idx, element):
    if list is None:
        return (None)
    copy = list[:]
    if idx < 0 or idx > len(copy):
        return (list)
    copy[idx] = element
    return (copy)
