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
