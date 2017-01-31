#!/usr/bin/python3
"""
Import BaseGeometry and use it for inheritance
Rectangle add functionality in the next few tasks
Did I do it right, Guillame?
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        init inherits from BaseGeometry
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns l * w
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        basic string representation
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
