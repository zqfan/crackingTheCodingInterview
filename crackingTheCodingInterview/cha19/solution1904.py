#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method which finds the maximum of two numbers. You should not
use if-else or any other comparison operator.
EXAMPLE
Input: 5, 10
Output: 10
"""

def max(a, b):
    """Return max of (a, b). a and b should be integer.

    if a > b: return a + 0 * (a - b)
    else return a + (-1) * (a - b)
    Note that in python,
    if x > 0, x >> x.bit_length() == 0, else == -1
    """
    x = a - b
    y = x >> x.bit_length()
    return a + y * x
