#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given an NxN matrix of positive and negative integers, write code to
find the sub matrix with the largest possible sum.
"""

def __get_base_block_sum(matrix):
    """
    get sum of sub matrix 0,0 to i,j
    sum(i, j) = sum(i-1, j) + sum(i, j-1)
                - sum(i-1, j-1) + matrix(i, j)

    return a function get_block_sum(row_start, col_start,
                                    row_end, col_end)
    which will return the sum of specific block
    """
    # base point 0,0
    sum_matrix = [[matrix[0][0]]]
    # first row
    for col in range(1, len(matrix[0])):
        sum_matrix[0].append(sum_matrix[0][col-1] + matrix[0][col])
    # first col
    for row in range(1, len(matrix)):
        sum_matrix.append([sum_matrix[row-1][0] + matrix[row][0]])
    # other cell
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            sum_matrix[row].append((sum_matrix[row][col-1] +
                                    sum_matrix[row-1][col] -
                                    sum_matrix[row-1][col-1] +
                                    matrix[row][col]))

    def get_block_sum(row_start, col_start, row_end, col_end):
        # if row_start < 0 and col_start < 0
        # means to get base block sum
        if row_start < 0 and col_start < 0:
            return sum_matrix[row_end][col_end]
        # if only row_start < 0
        if row_start < 0:
            return (sum_matrix[row_end][col_end] -
                    sum_matrix[row_end][col_start])
        if col_start < 0:
            return (sum_matrix[row_end][col_end] -
                    sum_matrix[row_start][col_end])
        # if block is base point
        if row_end == 0 and col_end == 0:
            return sum_matrix[0][0]
        # middle block
        return (sum_matrix[row_end][col_end] -
                sum_matrix[row_end][col_end - 1] -
                sum_matrix[row_end - 1][col_end] +
                sum_matrix[row_end - 1][col_end - 1])

    return get_block_sum


def get_max_sum(matrix):
    """Return max sum of sub matrix in matrix.

    there should be a O(n^3) algorithm using dynamic programming:
    for i in range(n):
      compute row max in arr[n*n], stands for max sum of sub matrix
                                   near the bound
      compute col max as the same
      compute the max one not near the bound
    compute the max one

    but here i still use O(n^4) method
    """
    if not matrix:
        return
    max_sum = matrix[0][0]
    get_block_sum = __get_base_block_sum(matrix)
    for row_start in range(len(matrix)):
        for row_end in range(row_start, len(matrix)):
            for col_start in range(len(matrix[0])):
                for col_end in range(col_start, len(matrix[0])):
                    block_sum = get_block_sum(row_start - 1,
                                              col_start - 1,
                                              row_end,
                                              col_end)
                    if max_sum < block_sum:
                        max_sum = block_sum
    return max_sum


if __name__ == '__main__':
    assert(get_max_sum([]) is None)
    assert(get_max_sum([[0]]) == 0)
    assert(get_max_sum([[1,1],[1,10]]) == 13)
