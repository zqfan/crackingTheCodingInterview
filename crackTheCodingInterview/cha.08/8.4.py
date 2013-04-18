#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.4
Write a method to compute all permutations of a string.
"""

def permutation(s):
    """Return all permutations of string s."""
    if len(s) == 1:
        return [s]
    result = []
    first = s[0]
    ss = s[1:]
    pers = permutation(ss)
    for p in pers:
        for i in range(0,len(p)):
            result.append(p[:i]+first+p[i:])
    return result


if __name__ == "__main__":
    r = permutation("main")
    for rr in r:
        print rr
