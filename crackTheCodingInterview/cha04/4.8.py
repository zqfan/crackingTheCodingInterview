#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
You are given a binary tree in which each node contains a value.
Design an algorithm to print all paths which sum up to that value.
Note that it can be any path in the tree - it does not have to start
at the root.
"""

def print_sum_path(root, value, path=[]):
    if not root:
        return
    path.append(root.data)
    tmp = 0
    for i in range(-len(path)+1,1):
        tmp += path[-i]
        if tmp == value:
            for v in path[-i:]:
                print v
    p = path[:]
    _check(root.left, value, p)
    _check(root.right, value, p)
