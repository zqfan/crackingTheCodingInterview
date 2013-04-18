#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.5
Implement an algorithm to print all valid (e.g., properly opened and
closed) combinations of n-pairs of parentheses.
EXAMPLE:
input: 3 (e.g., 3 pairs of parentheses)
output: ()()(), ()(()), (())(), ((()))

Analyse:
actually, there is another combination for n=3
(()())
"""

def parentheses(n):
    """Return a set of all valid n-pairs of parentheses."""
    if n < 1:
        return set([])
    if n == 1:
        return set(["()"])
    result = set([])
    r = parentheses(n-1)
    for rr in r:
        result.add("()"+rr)
        result.add(rr+"()")
        result.add("("+rr+")")
    return result


if __name__ == "__main__":
    r = parentheses(4)
    for rr in r:
        print rr
