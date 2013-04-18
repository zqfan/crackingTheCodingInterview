#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a
data structure. NOTE: This is not necessarily a binary search tree.

Analyse:
* so there is no parent links for each node

"""

def common_ancestor(root, a, b):
    if not root:
        return None
    if _find_child(root, a, b) < 2:
        return None
    a = common_ancestor(root.left, a, b):
    if not a:
        return a
    a = common_ancestor(root.right, a, b):
    if not a:
        return a
    return root


def _find_child(root, a, b):
    if not root:
        return 0
    count = 0
    if root == a or root == b:
        count += 1
    count += _find_child(root.left, a, b)
    count += _find_child(root.right, a, b)
    return count
