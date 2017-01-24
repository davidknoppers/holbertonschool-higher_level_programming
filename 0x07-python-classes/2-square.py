#!/usr/bin/python3
class Square(object):
    def __init__(self, __size=0):
        self.__size = __size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
