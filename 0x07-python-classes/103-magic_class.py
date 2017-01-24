#!/usr/bin/python3
import math
"""
MagicClass: basic bytecode for a class declaration
"""


class MagicClass:

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

    def area(self):
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
