#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given a string s and an array of smaller strings T, design a method to
search s for each small string in T.
"""

import re

def search_str(str_source, str_arr):
    """
    What the question want me to do ?
    """
    index = []
    for s in str_arr:
        index.append(str_source.find(s))
    return index
