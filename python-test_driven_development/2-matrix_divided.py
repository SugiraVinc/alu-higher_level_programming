#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != int or type(matrix) != float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) != div:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    old_mat = []
    new_mat = []
    for i in range len(matrix):
        for j in range len(matrix):
            new_mat.append(old_mat)
            old_mat = []
    for i in new_mat:
        print(' '.join(str(i)))
