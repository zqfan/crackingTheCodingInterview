#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.2
Imagine a robot sitting on the upper left hand corner of an NxN grid.
The robot can only move in two directions: right and down. How many
possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are “off limits”, such that the robot can not
step on them. Design an algorithm to get all possible paths for the
robot.
"""

def route_count(n, m):
    if n == 1 or m == 1:
        return 1
    return route_count(n-1, m) + route_count(n, m-1)

def print_all_route(n, m, rocks, path):
    if n < 1 or m < 1:
        return
    if rocks[n-1][m-1] == 1:
        return
    tmp = path[:]
    tmp.append((n,m))
    if n == 1 and m == 1:
        print u"-- path print start --"
        for i in range(0, len(tmp)):
            print tmp[i][0],tmp[i][1]
        print u"-- path print end --"
    print_all_route(n-1, m, rocks, tmp)
    print_all_route(n, m-1, rocks, tmp)

if __name__ == "__main__":
    import sys
    n = 3
    print route_count(n, n)
    rocks = ((0,0,0),(0,1,0),(0,0,0))
    print_all_route(3, 3, rocks, [])
