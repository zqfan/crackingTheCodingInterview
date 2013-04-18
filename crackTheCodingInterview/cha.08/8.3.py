#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.3
Write a method that returns all subsets of a set.
"""

def all_subsets(s):
    """Return all subsets of set s."""
    if not s:
        return [set([])]
    subsets = []
    ss = set.copy(s)
    e = ss.pop()
    r = all_subsets(ss)
    subsets.extend(r)
    for i in r:
        ii = i.copy()
        ii.add(e)
        subsets.append(ii)
    return subsets

if __name__ == "__main__":
    s = set("abc")
    subset = all_subsets(s)
    for ss in subset:
        print ss
