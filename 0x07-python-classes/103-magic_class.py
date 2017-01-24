#!/usr/bin/python3
import dis
class MagicClass(object):
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    def area(self):
        from math import pi
        return (self.__radius**2 * pi)
    def circumference(self):
        from math import pi
        return (self.__radius * 2 * pi)
print(dis.dis(MagicClass))
