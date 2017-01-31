#!/usr/bin/python3
"""
Module continues our basic study of inheritance
Square inherits from Rectangle
Rectangle inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Doesn't do too much
    """
    def __init__(self, size):
        """
        integer_validator is from 7-base_geometry
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
        return("[Square] {}/{}".format(self.__size, self.__size))
