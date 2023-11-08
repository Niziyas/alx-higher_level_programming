#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in i:
            new_matrix = pow(j, 2)
            print(new_matrix, end=" ")
        print()
square_matrix_simple(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
