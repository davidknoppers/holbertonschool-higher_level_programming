#!/usr/bin/python3
"""
Fancier Square featuring size and position
Getters and setters implemented for size and position
Requires a natural number for size
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError('size must be an integer')
        for i in position:
            if not isinstance(i, int):
                raise TypeError('size must be an integer')
        self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        errormsg = 'position must be a tuple of 2 positive integers'
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(errormsg)
        for i in value:
            if not isinstance(i, int):
                raise TypeError(errormsg)
        self.__position = value

    def my_print(self):
        print("\n" * self.__position[1], end="")
        print("\n".join([" " * self.position[0] + "#" * self.__size
                         for i in range(self.__size)]))
