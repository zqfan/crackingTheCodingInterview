#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Describe an algorithm to find the largest 1 million numbers in 1
billion numbers. Assume that the computer memory can hold all one
billion numbers.
"""

def get_max_million_numbers(billion_numbers):
    """
    4Bytes * 1,000,000,000 = 4 GB
    4Bytes * 1,000,000 = 4 MB

    # n*log(n)
    1. divide billion_numbers to 100 parts, using n*log(n) sort
    2. merge 100 parts, get the first million numbers

    # n*log(m)
    1. divide billion_numbers to 100 parts, using min heap sort, just
    hold million numbers in heap
    2. transfer all 100 heaps to max heap, take the first million
    numbers

    # O(n)
    if our memory is large enough, then we can find kth number in
    O(n) time (expected time), and walk through billion numbers, print
    larger or equal numbers
    """
    pass
