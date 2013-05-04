#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given a two dimensional graph with points on it, find a line which
passes the most number of points.
"""

from solution1005 import Point, get_line

def get_most_points_line(points):
    """Return the line across most points.

    if the line is vertical, return x = b in the format of (b, 0)
    else return y = kx + b in the format of (k, b)
    """
    count = {}
    # compute all lines
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            line = get_line(points[i], points[j])
            if not line:
                continue
            if count.get(line):
                count[line] += 1
            else:
                count[line] = 1
    if not count:
        return
    # sort lines in decreasing order
    lines = sorted(count.iteritems(), key=lambda x: x[1], reverse=True)
    return lines[0][1]
