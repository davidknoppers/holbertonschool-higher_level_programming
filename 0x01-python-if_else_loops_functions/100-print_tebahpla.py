#!/usr/bin/python3
for ord_num in range(122, 96, -1):
    if ord_num % 2 != 0:
        ord_num -= 32
    print(chr(ord_num), end="")
