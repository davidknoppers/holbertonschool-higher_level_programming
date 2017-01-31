#!/usr/bin/python3
"""
Import BaseGeometry and use it for inheritance
Rectangle adds functionality in the next few tasks
Did I do it right, Guillame?
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        init method inherits integer validators from previous task
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
