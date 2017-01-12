#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return (None)
    if my_list == []:
        return ([])
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return (my_list)
