#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raws in matrix:
        j = 0
        for i in raws:
            if j == (len(raws) -1):
                print("{d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            j +=1
        print("")
