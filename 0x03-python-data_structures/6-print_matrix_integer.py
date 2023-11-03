#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join("{:d}".format(j) for j in i))
    print("--")
print_matrix_integer(matrix=[[1,2,3],[4,5,6],[7,8,9]])
