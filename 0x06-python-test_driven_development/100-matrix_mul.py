#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]] or m_a == [[], []]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or m_b == [[], []]:
        raise TypeError("m_b can't be empty")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for row in range(len(m_b[0]))] for col in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
