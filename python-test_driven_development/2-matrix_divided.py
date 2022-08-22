#!/usr/bin/python3
""" We are doing a matrix unittest """


def matrix_divided(matrix, div):
    """ A matrix function that will help us test """

    for raw in matrix:
        if type(raw) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for data in raw:
            if type(data) != int and type(data) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    raw_size = len(matrix[0])
    for raw in matrix:
        if len(raw) != raw_size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list())
        for x in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][x] / div, 2))
    return new_matrix
