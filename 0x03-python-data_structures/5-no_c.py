#!/usr/bin/python3
def no_c(str):
    result = ""
    for char in str:
        if char != 'c' and char != 'C':
            result += char
    return (result)
