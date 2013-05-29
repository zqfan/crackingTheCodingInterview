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
    result_set = set([])

    def get_paren_pair(left, right, parens):
        if (left < 0 or right < left):
            return
        if (left == 0 and right == 0):
            result_set.add(parens)
            return
        if (left > 0):
            new_parens = parens + '('
            get_paren_pair(left - 1, right, new_parens)
        if (right > left):
            new_parens = parens + ')'
            get_paren_pair(left, right - 1, new_parens)

    get_paren_pair(n, n, '')
    return result_set


if __name__ == "__main__":
    r = parentheses(4)
    for rr in r:
        print rr
