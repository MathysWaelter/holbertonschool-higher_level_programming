#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_tmp = []
    if len(matrix) > 0:
        for i in matrix[:]:
            matrix_tmp.append(list(map(lambda x: x ** 2, i)))
    return matrix_tmp
