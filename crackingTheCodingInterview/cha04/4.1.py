#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one.
"""

def is_balance_tree(binary_tree):
    """Using DFS to check a binary tree if it is a balance tree."""
    def _min_max_depth(binary_tree):
        if not binary_tree:
            return (-1,-1)
        (left_min, left_max) = _min_max_depth(binary_tree.left)
        (right_min, right_max) = _min_max_depth(binary_tree.right)
        min_dep = left_min if left_min < right_min else right_min
        max_dep = left_max if left_max > right_max else right_max
        return (min_dep + 1, max_dep + 1)

    (min_dep, max_dep) = _min_max_depth(binary_tree)
    if max_dep - min_dep > 1:
        return False
    return True


def test():
    import binary_tree
    bt = binary_tree.BinaryTree()
    for i in range(1,4):
        bt.random_insert(i)
    print is_balance_tree(bt.root)

if __name__ == "__main__":
    test()
