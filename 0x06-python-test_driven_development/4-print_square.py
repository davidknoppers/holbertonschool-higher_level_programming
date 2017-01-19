#!/usr/bin/python3
"""
print_square: prints a square of hashes
@size: int size indicating dimensions of square
Size must be a positive integer
"""


def print_square(size):
    """
    prints a square of hashes
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            if j < (size - 1):
                print("#", end="")
            else:
                print("#")
