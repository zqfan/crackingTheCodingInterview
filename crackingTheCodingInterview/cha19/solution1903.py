#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write an algorithm which computes the number of trailing zeros in n
factorial.
"""

def trailing_zeros(n):
    """Return trailing zeros of n factorial.

    trailing zero means 10=2*5, since there is always an even number
    in front of 5, so each 5 contributes a zero, and 5^x contributes
    x zeros
    """
    r = 0
    while n > 0:
        n /= 5
        r += n
    return r
