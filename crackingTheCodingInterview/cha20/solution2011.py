#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Imagine you have a square matrix, where each cell is filled with
either black or white. Design an algorithm to find the maximum
sub square such that all four borders are filled with black pixels.
"""

def __check_square(matrix, start_r, start_c, n):
    # check if row is out of bound
    if start_r + n > len(matrix):
        return False
    # top row already checked
    # so check left col, right col and bottom row
    for i in range(n):
        if matrix[start_r+i][start_c]:
            return False
        if matrix[start_r+i][start_c+n-1]:
            return False
        if matrix[start_r+n-1][start_c+i]:
            return False
    return True

def get_max_black_square(matrix, row, threshold):
    n = len(matrix[row])
    col = 0
    max_col = 0
    while col < n:
        # ignore white and continue
        if matrix[row][col]:
            col += 1
            continue
        # the remain cell is less than threshold, then return
        if col + threshold >= n:
            return (max_col, threshold)
        found = True
        # start to try continuous black cell bigger than threshold
        for t in range(1, threshold+1):
            # but there is a white cell, then break
            if matrix[row][col+t]:
                found = False
                break
        # there is no larger continuous black cell, then jump over
        if not found:
            col += t
            continue
        # try to find the max
        for right in range(col+threshold, n):
            # if there is a white cell, then break
            if matrix[row][right]:
                break
            # if there is a larger sub square, then update
            if __check_square(matrix, row, col, right-col+1):
                threshold = right-col+1
                max_col = col
        col += 1
    return (max_col, threshold)


def maximum_sub_square(square_matrix):
    """Brute force O(N^3)

    square_matrix is a matrix of 0 and 1, 0 means black, 1 means white
    return the maximum sub square in tuple (start_r, start_c, size)
    """
    if not square_matrix:
        return (0, 0, 0)
    n = len(square_matrix)
    start_r, start_c, size = 0, 0, 0
    for i in range(n):
        # if there is no hope to find larger one, then break
        if i + size >= n:
            break
        # O(n^n)
        new_c, new_size = get_max_black_square(square_matrix, i, size)
        if new_size > size:
            start_r = i
            start_c = new_c
            size = new_size
    return (start_r, start_c, size)


if __name__ == '__main__':
    print maximum_sub_square([])
    print maximum_sub_square([[0,1],[1,1]])
    print maximum_sub_square([[1,1],[0,0]])
    print maximum_sub_square([[1,1],[1,1]])
    print maximum_sub_square([[0,0,0],[0,0,0],[0,0,0]])
