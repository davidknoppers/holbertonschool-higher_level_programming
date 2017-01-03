#!/usr/bin/python3
def print_last_digit(number):
    digit = str(number)
    digit = digit[-1]
    digit = int(digit)
    print(digit, end="")
    return digit
