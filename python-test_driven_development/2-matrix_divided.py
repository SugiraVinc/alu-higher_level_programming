#!/usr/bin/python3
""" We are doing a matrix unittest """


def matrix_divided(matrix, div):
    """ A matrix function that will help us test """
    if type(matrix) != int or type(matrix) != float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for raw in matrix:
        if len(matrix) != len(raw):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    old_mat = []
    new_mat = []
    for i in len(matrix):
        for j in len(matrix):
            new_mat.append(old_mat)
            old_mat = []
    for i in new_mat:
        print(' '.join(str(i)))
