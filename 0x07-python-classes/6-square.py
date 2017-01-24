#!/usr/bin/python3
"""
Fancier Square featuring size and position
Getters and setters implemented for size and position
Requires a natural number for size
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize square with size and pos
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    def area(self):
        """
        return area by squaring size
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        getter for size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(errormsg)
        self.__size = value

    @property
    def position(self):
        """
        getter for pos
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        setter for pos
        """
        errormsg = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple:
            raise TypeError(errormsg)
        if len(value) != 2:
            raise TypeError(errormsg)
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(errormsg)
        self.__position = value

    def my_print(self):
        """
        wild print function
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)]))
