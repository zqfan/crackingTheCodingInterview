#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
9.6
Given a matrix in which each row and each column is sorted, write
a method to find an element in it.

Analyse:
i assume they are sorted by increasing order. */
"""

def binary_search(array, start, end, element):
    if start > end:
        return -1
    if start == end:
        return start if array[start] == element else -1
    m = ( start + end ) / 2
    if array[m] == element:
        return m
    elif array[m] > element:
        return binary_search(array, start, m - 1, element)
    else:
        return binary_search(array, m + 1, end, element)


def get_pos(matrix, element):
    """Get position of element in matrix.

    Matrix is sorted in increasing order both in row and column.
    """
    first_col = [r[0] for r in matrix]
    if element < first_col[0]:
        return -1
    row_index = len(first_col) - 1
    for i in range(1, len(first_col)):
        if element < first_col[i]:
            row_index = i - 1;
            break
    col_index = binary_search(matrix[row_index],
                              0,
                              len(matrix[row_index]) - 1,
                              element)
    return (row_index, col_index)


if __name__ == "__main__":
    m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    print get_pos(m,9)
