#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
You have two very large binary trees: T1, with millions of nodes, and
T2, with hundreds of nodes. Create an algorithm to decide if T2 is a
subtree of T1.

Analyse:
on 64-bit system, a node need at least 8*2+8=24Bytes, with millions of
nodes, which means more than 24MB RAM allocated.
asume T1 has M node and T2 has N node, O(M*N) is too large.
"""

def is_subtree(btree1, btree2):
    """Judge if binary tree btree2 is subtree of binary tree btree1"""
    if not btree2:
        return True
    _is_subtree(btree1, btree2)


def _is_subtree(btree1, btree2):
    """Judge if binary tree btree2 is subtree of binary tree btree1"""
    if not btree1:
        return False
    if btree1.data == btree2.data:
        l = match_btree(btree1.left, btree2.left)
        r = match_btree(btree1.right, btree2.right)
        if l and r:
            return True
    l = _is_subtree(btree1.left, btree2)
    r = _is_subtree(btree1.right, btree2)
    return l or r


def match_btree(btree1, btree2):
    if not btree1 and not btree2:
        return True
    if not btree1 or not btree2:
        return False
    if btree1.data != btree2.data:
        return False
    l = match_btree(btree1.left, btree2.left)
    r = match_btree(btree1.right, btree2.right)
    return l and r
