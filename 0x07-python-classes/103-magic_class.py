#!/usr/bin/python3
import dis
import math
class MagicClass(object):
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = 0

    def area(self):
        from math import pi
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (self.__radius * 2 * math.pi)
print(dis.dis(MagicClass))
