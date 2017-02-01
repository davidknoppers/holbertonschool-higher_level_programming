"""
MyInt challenges us to change the basics of an int
== is !=
!= is ==
"""


class MyInt(int):
    def __new__(cls, value):
        """
        create a new instance of class cls
        """
        return super().__new__(cls, value)

    def __eq__(self, other):
        """
        !=
        """
        return self - other is not 0

    def __ne__(self, other):
        """
        ==
        """
        return self - other is 0
