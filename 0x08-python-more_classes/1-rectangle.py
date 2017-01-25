#!/usr/bin/python3
"""
Fancier Rectangle featuring width and height
Getters and setters implemented for width and height
Requires natural numbers for width and height
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        initialize rectangle with width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        getter for pos
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
