#!/usr/bin/python3
def new_in_list(list, idx, element):
    copy = list[:]
    if idx > len(copy):
        return (copy)
    copy[idx] = element
    return (copy)
