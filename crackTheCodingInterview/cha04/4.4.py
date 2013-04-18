#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
Given a binary search tree, design an algorithm which creates a linked list of all the
nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).

Analyse:
* I don't know why it's must a BST.
"""

def gen_linklist_by_depth(bst):
    """Generate linked lists store the nodes for each depth."""
    linked_list = [[bst]]
    cur_dep = linked_list[0]
    while True:
        next_dep = []
        for node in cur_dep:
            if node.left:
                next_dep.append(node.left)
            if node.right:
                next_dep.append(node.right)
        if not next_dep:
            break
        linked_list.append(next_dep)
        cur_dep = next_dep
    return linked_list
