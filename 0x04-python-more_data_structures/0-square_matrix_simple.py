#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return (None)
    if matrix == []:
        return ([])
    squared_matrix = [[x*x for x in row] for row in matrix]
    return (squared_matrix)
