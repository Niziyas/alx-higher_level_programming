#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        new_row = [pow(element, 2) for element in row]
        print(new_row)

square_matrix_simple(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
