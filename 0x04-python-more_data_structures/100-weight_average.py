#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return (sum(num[0] * num[1] for num in my_list)
            / sum(num[1] for num in my_list))
