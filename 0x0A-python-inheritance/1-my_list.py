#!/usr/bin/python3
"""
This module demonstrates basic inheritance
MyList inherits from list and we add a simple method
And by simple I mean exhaustively error-checked
"""


class MyList(list):
    """
    This module demonstrates basic inheritance
    MyList inherits from list and we add a simple method
    And by simple I mean exhaustively error-checked
    """

    def print_sorted(self):
        """
        error checks the list and then prints it, sorted
        """
        print(sorted(self))
