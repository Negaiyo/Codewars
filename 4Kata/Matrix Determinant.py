# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python

def determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        minor = get_minor(matrix, 0, c)
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det


def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


# import numpy as np
#
# def determinant(a):
#     return round(np.linalg.det(np.matrix(a)))