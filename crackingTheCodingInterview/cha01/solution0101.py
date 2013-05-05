#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Implement an algorithm to determine if a string has all unique
characters. What if you can not use additional data structures?
"""

def is_unique_str_v1(s):
    """Determine a string has all unique characters.

    Only support ASCII string
    """
    if not isinstance(s, str):
        return False
    return len(s) == len(set(s))


def is_unique_str(s):
    """Determine a string has all unique characters.

    Only support ASCII string, O(n^2) algorithm
    """
    if not isinstance(s, str):
        return False
    for c in s:
        if s.count(c) > 1:
            return False
    return True
