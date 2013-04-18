#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
Given a directed graph, design an algorithm to find out whether there is a route be-
tween two nodes.
"""

def is_routable(from_vertex, to_vertex):
    """Using BFS to test a route between two vertex."""
    done = []
    todo = [from_vertex]
    while True:
        v = todo[0]
        if not v:
            return False
        if v == to_vertex:
            return True
        del todo[0]
        done.append(v)
        for vertex in v.next_hops():
            if vertex not in done:
                todo.append(vertex)
