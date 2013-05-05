#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Design an algorithm to find the kth number such that the only prime
factors are 3, 5, and 7.

Analyze:
f(1) = 1
f(k) = min{f(i)*3, f(i)*5, f(i)*7} i=1...k-1

Analyze:
A(3,0) = 1, (1)
A(3,1) = 3, A(3,0)*(3, 5, 7)
A(3,2) = 9, A(3,1)*(3, 5, 7)
A(3,3) = 27, A(3,2)*(3, 5, 7)

f(13) = 63, 9 < 13 < 27
(9, 15, 21, 25, 35, 49) U (27, 45, 63)
"""

def f1(k):
    """O(n*n) algo"""
    if k < 1:
        return 0
    r = [0, 1]
    for i in range(2, k + 1):
        n = [x * 3 for x in r if x * 3 > r[-1]]
        n.extend([x * 5 for x in r if x * 5 > r[-1]])
        n.extend([x * 7 for x in r if x * 7 > r[-1]])
        r.append(min(n))
    return r[k]


def f(k):
    """O(n) algo"""
    if k < 1:
        return 0
    # q3 contains all numbers n = 3^x, x >= 1
    # q5 contains all numbers n = 3^x * 5^y, x >=0, y >= 1
    # q7 contains all numbers n = 3^x * 5^y * 7^z, x,y >= 0, z >= 1
    r, q3, q5, q7 = [1], [3], [5], [7]
    for i in range(1, k):
        n = min(q3[0], q5[0], q7[0])
        r.append(n)
        if n == q3[0]:
            q3.append(n*3)
            q5.append(n*5)
            q7.append(n*7)
            del q3[0]
        elif n == q5[0]:
            q5.append(n*5)
            q7.append(n*7)
            del q5[0]
        else:
            q7.append(n*7)
            del q7[0]
    return r[k - 1]
