#!/usr/bin/python3
def element_at(list, idx):
    if idx < 0:
        return(None)
    if idx < len(list):
        return(list[idx])
    return (None)
