#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given an integer, print the next smallest and next largest number that have the same number of 1 bits in their binary representation.
"""

def neighbour_bf(n):
    """Brute force solution

    Return next smallest and next largest number that have the same
    number of 1 bits in their binary representation.
    """
    if n == 0:
        return (0, 0)
    count = bin(n).count('1')
    small = n - 1
    while True:
        if count == bin(small).count('1'):
            break
        small -= 1
    big = n + 1
    while True:
        if count == bin(big).count('1'):
            break
        big += 1
    return (small, big)


def neighbour(n):
    if n == 0:
        return (0, 0)
    if n < 0:
        r = _neighbour(-n)
        return (-r[1], -r[0])
    return _neighbour(n)


def _neighbour(n):
    """n must be positive"""
    s = bin(n)[2:]
    # find the largest
    # find 01 seq from right to left
    s1 = '0' + s
    i = s1.rfind('01')
    # turn 01 seq to 10, increasing 2^j - 2^(j-1), j = len(s1)-i-2
    s2 = '0b' + s1[:i] + '10'
    # shift right 1 bits to right end
    s3 = s1[i+2:].rstrip('0')
    s2 = s2 + '0'*(len(s1[i+2:]) - len(s3)) + s3
    big = int(s2, 2)
    # find the smallest
    # in python, int is not specific to certain bits,
    # so if a number gets full 1 bit, for example, n == 7
    # it simply be -n, which is -7, not 11100000
    if n.bit_length() == s.count('1'):
        return (-n, big)
    # find 10 seq from right to left
    i = s.rfind('10')
    s2 = '0b' + s[:i] + '01'
    # shift right 1 bits to left
    s3 = s[i+2:].lstrip('0')
    s2 = s2 + s3 + '0'*(len(s[i+2:]) - len(s3))
    small = int(s2, 2)
    return (small, big)