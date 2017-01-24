#!/usr/bin/python3
"""
Most advanced square yet!
Holds a size and position and can print using repr
requires ints
"""


class Square(object):
    """
    basic features
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >=0')
        self.__position = position
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError(errormsg)
        for i in position:
            if not isinstance(i, int):
                raise TypeError(errormsg)

    def area(self):
        """
        basic features
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        basic features
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        basic features
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    @property
    def position(self):
        """
        basic features
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        basic features
        """
        errormsg = 'position must be a tuple of 2 positive integers'
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(errormsg)
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(errormsg)
        self.__position = value

    def string(self):
        """
        strings result
        """
        if self.__size == 0:
            print("")
        else:
            result = ''
            for i in range(self.__position[1]):
                result += '\n'
            for i in range(self.__size):
                result += ' ' * self.__position[0] + self.__size * '#'
                if i < self.size - 1:
                    result += '\n'
            return (result)

    def my_print(self):
        """
        basic features
        """
        return (self.string())

    def __repr__(self):
        """
        basic features
        """
        return(self.string())
