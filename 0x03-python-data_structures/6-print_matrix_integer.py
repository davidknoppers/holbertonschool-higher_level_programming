#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_array = []
    for row in matrix:
        row_array.append(' '.join('{:d}'.format(item) for item in row))
    print('\n'.join(row_array))
