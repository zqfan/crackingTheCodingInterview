#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
Write an algorithm to find the ‘next’ node (i.e., in-order successor)
of a given node in a binary search tree where each node has a link to
its parent.

Analyse:
"""

def next_node(node):
    """Find next node of a given node in a BST.

    NOTE: the BST node must have a link to its parent.
    """
    # is root
    if not node.parent:
        return _min_node(node.right)
    # is subtree and is left
    if node.parent.left == node:
        if not node.right:
            return node.parent
        return _min_node(node.right)
    # is subtree and is right
    return node.parent.parent


def _min_node(node):
    """Return the min node of a BST subtree."""
    if not node:
        return None
    i = node
    while i.left:
        i = i.left
    return i
