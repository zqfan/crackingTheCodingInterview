#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
You are given an array of integers (both positive and negative). Find
the continuous sequence with the largest sum. Return the sum.
EXAMPLE
Input: {2, -8, 3, -2, 4, -10}
Output: 5 (i.e., {3, -2, 4} )
"""

def max_sum_continuous_sequence(arr):
    if not arr:
        return 0
    max_sum, tmp_sum = arr[0], 0
    for i in arr:
        tmp_sum += i
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        if tmp_sum < 0:
            tmp_sum = 0
    return max_sum
