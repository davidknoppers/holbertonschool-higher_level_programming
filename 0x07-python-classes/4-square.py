#!/usr/bin/python3
"""
Square -demonstrates basic components of OOP

Contains Square and a few attributes
"""


class Square:
    """
    Creates a square based on size
    Offers basic operations like setters and getters
    Also offers an area function
    """
    def __init__(self, size=0):
        """
        initializes square with a given size or size = 0
        """
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        returns area by squaring size
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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
