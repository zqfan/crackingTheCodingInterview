#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Numbers are randomly generated and passed to a method. Write a program
to find and maintain the median value as new values are generated.
"""

import bisect


def maintain_median():
    __arr = []

    def insert(n):
        # O(n) ?
        # or using two heap? O(logn)
        bisect.insort(__arr, n)
        length = len(__arr)
        if length % 2 == 1:
            return __arr[length/2]
        else:
            return (__arr[length/2] + __arr[length/2 - 1]) / 2.0
    return insert


if __name__ == '__main__':
    m = maintain_median()
    for i in range(10):
        print m(i)
