#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method to count the number of 2s between 0 and n.
"""

def get_digit_count(n):
    """
    there will be a 2 digit in every 10 number,
    there will be 10 2x digit in every 100 number,
    and so on
    """
    d = 2
    # get positive n
    pn = abs(n)
    count = 0
    factor = 1
    cur_number = 0
    while pn > 0:
        # get pn last digit
        last_digit = pn % 10
        # get cur_number
        cur_number += last_digit * factor
        # get count of 2 in factor pos
        count += factor * (pn / 10)
        # last digit larger than or equal to 2
        if last_digit > d:
            count += factor
        # last digit equal to 2, count the low number
        elif last_digit == d:
            count += cur_number - d * factor + 1
        factor *= 10
        pn /= 10
    return count
