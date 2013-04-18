#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.7
Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents) and pennies (1 cent), write code to calculate the
number of ways of representing n cents.
"""

def get_all_combanition(n):
    """return a set of all combanitions."""
    if n < 0:
        return []
    result = []
    def _get_all_combanition(n, i):
        if n > i:
            r = get_all_combanition(n-i)
            for rr in r:
                rr.append(i)
            return r
        elif n == i:
            return [[i]]
        else:
            return []

    result.extend(_get_all_combanition(n,1))
    result.extend(_get_all_combanition(n,5))
    result.extend(_get_all_combanition(n,10))
    result.extend(_get_all_combanition(n,25))
    # remove duplicate combanition
    nodup = []
    for r in result:
        # since list is a order sensitive
        r.sort()
        if not r in nodup:
            nodup.append(r)
    return nodup

if __name__ == "__main__":
    import sys
    print get_all_combanition(int(sys.argv[1]))
