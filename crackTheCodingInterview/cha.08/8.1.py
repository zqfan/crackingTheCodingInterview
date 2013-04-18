#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.1	 Write a method to generate the nth Fibonacci number.
"""

def fibonacci(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n, result=None):
    if not result:
        result = []
        for i in range(0,n+1):
            result.append(0)
    if n < 1:
        return 0
    if n < 3:
        result[n] = 1
        return 1
    if result[n-1] == 0:
        result[n-1] = fibonacci2(n-1, result)
    if result[n-2] == 0:
        result[n-2] = fibonacci2(n-2, result)
    return result[n-1] + result[n-2]


def fibonacci3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

if __name__ == "__main__":
    import sys
    print fibonacci3(int(sys.argv[1]))
