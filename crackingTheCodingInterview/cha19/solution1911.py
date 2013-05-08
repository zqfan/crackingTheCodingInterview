#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Design an algorithm to find all pairs of integers within an array
which sum to a specified value
"""

def get_all_pairs_bf(sum, integers):
    """Brute force, O(n*n)"""
    pairs = []
    for i in integers:
        # find pair and if this pair not exist yet
        # note that (1, 2) is same as (2, 1) but different from (1, 2)
        # which means, [1, 1, 2] only get (1, 2) for sum 3
        flag = (sum - i) in integers and not (sum - i, i) in pairs
        flag = flag and integers.count(i) == integers.count(sum - i)
        # if (x, x) is a pair but integers only have one x, then deny
        if i == sum - i and integers.count(i) == 1:
            flag = False
        if flag:
            pairs.append((i, sum - i))
    if (0, 0) in pairs and integers.count(0) < 2:
        pairs.remove((0, 0))
    return pairs


def get_all_pairs(sum, integers):
    """return all pairs of integers which summary is sum, O(nlogn)"""
    if not integers:
        return []
    tmp = integers[:]
    tmp.sort()
    pairs = []
    start, end = 0, len(tmp) - 1
    while start < end:
        r = tmp[start] + tmp[end]
        if r == sum:
            pairs.append((tmp[start], tmp[end]))
            end -= 1
        elif r > sum:
            # then decrease the right hand side
            end -= 1
        else: # if r < sum
            # then increase the left hand side
            # this is safe, because the larger right hand side already
            # try, if that is a pair, the smaller left hand side
            # should be paired, not this one
            start += 1
    return pairs
