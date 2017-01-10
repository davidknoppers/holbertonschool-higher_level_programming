#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_ints = [0, 0]
    b_ints = [0, 0]

    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len > 2:
        a_len = 2
    if b_len > 2:
        b_len = 2

    for i in range(a_len):
        a_ints[i] += tuple_a[i]
    for i in range(b_len):
        b_ints[i] += tuple_b[i]

    result = (a_ints[0] + b_ints[0], a_ints[1] + b_ints[1])

    return (result)
