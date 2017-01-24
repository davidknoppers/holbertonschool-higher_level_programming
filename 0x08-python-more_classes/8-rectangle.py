#!/usr/bin/python3
"""
Fancier Rectangle featuring width and height
Getters and setters implemented for width and height
Requires natural numbers for width and height
"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize rectangle with width and height
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if value < 0:
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
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    def area(self):
        """
        area of a rectangle
        """
        return self.__height * self.__width
    def perimeter(self):
        """
        perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
    def __str__(self):
        """
        constructs grid output for rectangle
        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(self.__height):
            result += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                result += '\n'
        return result
    def __repr__(self):
        """
        formats basic text representation of rectangle
        """
        result = "Rectangle({}, {})".format(self.__width, self.__height)
        return result
    def __del__(self):
        """
        deletes an instance and updates class count
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the larger of the two rectangles, after input checks
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
