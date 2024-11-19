#!/usr/bin/python3
"""matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    :param matrix: 2D list to rotate
    """
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to achieve a 90-degree clockwise rotation
    for row in matrix:
        row.reverse()
