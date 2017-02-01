#!/usr/bin/python3
"""
Class getting fancier now!
BG is not supposed to have an area function
integer_validator will be inherited by other classes
"""


class BaseGeometry:
    def area(self):
        """
        Intentionally unimplemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates int input
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
