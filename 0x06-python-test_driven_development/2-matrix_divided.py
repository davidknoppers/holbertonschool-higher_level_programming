#!/usr/bin/python3
"""
matrix_divided - divides each element of a matrix by given divisor
Returns a whole suite of errors in response to bad input
Returns a new matrix with the newly calculated elements
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix divided by div
    """
    lol_error = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or not isinstance(matrix, list):
        raise TypeError(lol_error)
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(lol_error)
    if not isinstance(div, (int, float)) or div == False or div == True:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    nested_check = any(not isinstance(i, list) for i in matrix)
    if nested_check:
        raise TypeError(lol_error)
    row_0 = len(matrix[0])
    for row in matrix:
        if row_0 != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(lol_error)
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return (result)
