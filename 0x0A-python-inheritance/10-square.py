#!/usr/bin/python3
"""
Square inherits from rectangle and some items are overwritten
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle, but with size instead of l/w
    """
    def __init__(self, size):
        """
        init with inheritance from BaseGeometry
        """
        size = super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns s * s
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        basic string representation
        """
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
