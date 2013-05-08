#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method to randomly generate a set of m integers from an array
of size n. Each element must have equal probability of being chosen
"""

import random


def get_random_set(m, arr):
    """Get random set of size m from arr

    Each element of return set has same probability
    """
    # remove duplicate elements from arr
    # if we don't, then when we select two same elements from arr
    # and target set will just accept one, then the probability will
    # not be same
    tmp = list(set(arr))
    target_set = set()
    for i in range(m):
        x = random.randint(0, len(tmp)-1)
        target_set.add(tmp[x])
        # delete the selected element from arr
        # if we don't, same value can be selected
        del tmp[x]
    return list(target_set)
