#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method to generate a random number between 1 and 7, given a
method that generates a random number between 1 and 5 (i.e., implement
rand7() using rand5())
"""

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    """return randint(1,7) using rand5.

    1. create a large continuous range using rand5(), actually, for
    range [0, 5^n), you can do 5^(n-1)*rand5() + 5^(n-2)*rand5() +
    ... + 5^0*rand5(), they are continuous and each probability is
    1/5^n, since rand5() = [1,5], not [0, 4], the above formulate has
    slight difference
    2. take first 7*n of these value, each of them has same
    probability, calculate their mod of 7, so [0, 6) has same
    probability which is n/(5^n)
    3. from the point view of output, each output value has same
    probability, that enough
    """
    while True:
        # assume n == 2
        x = 5 * (rand5() - 1)+ (rand5() - 1)
        if x < 14:
            return x % 7 + 1
