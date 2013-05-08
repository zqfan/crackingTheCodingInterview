#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a function that adds two numbers. You should not use + or any
arithmetic operators.
"""

def add(a, b):
    """
    using bit operators instead of arithmetic op
    Note that in python -1 >> n == -1, so this function doesn't
    support negative numbers

    a = 1011, b = 0101, a + b = 10000
    a | b = 1111, add but without carrying and with false bits
    a & b = 0001, carrying bit
    a ^ b = 1110, add but without carrying bit
    so: a + b = (a ^ b) + (a & b) << 1
    """
    if a < 0 or b < 0:
        return
    r = a
    while b != 0:
        r, b = r ^ b, (r & b) << 1
    return r
