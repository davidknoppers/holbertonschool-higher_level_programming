#!/usr/bin/python3
def replace_in_list(list, idx, element):
    if idx < 0 or idx > len(list):
        return(list)
    list[idx] = element
    return(list)
