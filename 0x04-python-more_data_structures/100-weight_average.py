#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    result = sum(num[0] * num[1] for num in my_list)
    result /= sum(num[1] for num in my_list)
    return (result)
