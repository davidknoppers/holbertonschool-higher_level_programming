#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return (None)
    seen = []
    result = 0
    for i in my_list:
        if i not in seen:
            result += i
        if i not in seen:
            seen.append(i)
    return (result)
