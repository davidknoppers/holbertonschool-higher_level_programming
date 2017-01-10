#!/usr/bin/python3
def new_in_list(mylist, idx, element):
    if mylist is None:
        return (None)
    copy = mylist[:]
    if idx < 0 or idx >= len(copy):
        return (mylist)
    copy[idx] = element
    return (copy)
