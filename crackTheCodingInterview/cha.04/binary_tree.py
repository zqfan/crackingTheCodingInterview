#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random


class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def random_insert(self, data, parent=None):
        n = BinaryTreeNode(data)
        if not self.root:
            self.root = n
            return
        if not parent:
            parent = self.root
        if parent and (not isinstance(parent, BinaryTreeNode)):
            parent = self.root
        self._random_insert(parent, n)

    def _random_insert(self, parent, child):
        r = random.randint(0, 1)
        if r > 0:
            if not parent.left:
                parent.left = child
            else:
                self._random_insert(parent.left, child)
        else:
            if not parent.right:
                parent.right = child
            else:
                self._random_insert(parent.right, child)

    def full_insert(self, data):
        n = BinaryTreeNode(data)
        if not self.root:
            self.root = n
            return
        nodes = [self.root]
        while len(nodes) > 0:
            node = nodes[0]
            del nodes[0]
            if node.left:
                nodes.append(node.left)
            else:
                node.left = n
                return
            if node.right:
                nodes.append(node.right)
            else:
                node.right = n
                return

    def pre_order(self, root=None):
        if not root:
            return
        print root.data
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root=None):
        if not root:
            return
        self.in_order(root.left)
        print root.data
        self.in_order(root.right)

    def post_order(self, root=None):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print root.data


def test():
    bt = BinaryTree()
    for i in range(0,5):
        bt.full_insert(i)
    bt.pre_order(bt.root)
    bt.in_order(bt.root)
    bt.post_order(bt.root)


if __name__ == "__main__":
    test()
