#!/usr/bin/python3
"""
MyInt challenges us to change the basics of an int
== is !=
!= is ==
"""


class MyInt(int):
    """
    Reworking int to switch == and !=
    *
    *
    """
    def __new__(cls, value):
        """
        create a new instance of class cls
        """
        return super().__new__(cls, value)

    def __eq__(self, other):
        """
        !=
        """
        if super().__eq__(other):
            return False
        return True

    def __ne__(self, other):
        """
        ==
        """
        if self.__eq__(other):
            return False
        return True
