#!/usr/bin/python3
"""
matrix_divided - divides each element of a matrix by given divisor
Returns a whole suite of errors in response to bad input
Returns a new matrix with the newly calculated elements
"""


def matrix_divided(matrix, div):
    """
    matrix_divided returns a  new matrix divided by div
    """
    lol_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(lol_error)
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError(lol_error)
    if len(matrix[0]) == 0:
        raise TypeError(lol_error)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if isinstance(item, (int, float)):
                item = int(item)
            else:
                raise TypeError(lol_error)
        if div == 0:
            raise ZeroDivisionError('division by zero')
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result
