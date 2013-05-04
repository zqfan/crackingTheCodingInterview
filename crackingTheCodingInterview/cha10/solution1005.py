#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

""" solution cha10-05

Given two squares on a two dimensional plane, find a line that would
cut these two squares in half.
"""

class Point(object):
    det = 0.000001

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return all((abs(self.x - point.x) < self.det,
                   abs(self.y - point.y) < self.det))


class Square(object):
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


def get_square_center(square):
    x = (square.left.x + square.right.x)/2.0
    y = (square.top.y + square.bottom.y)/2.0
    return Point(x, y)


def get_line(point1, point2):
    """return (k,b) of a line in format of y = kx + b.

    if point1 == point2; then return None
    if the line is x = k1, then return (k1,)
    else return (k, b), you must use len(r) to judge the case
    """
    # same point
    if point1 == point2:
        return
    # vertical line
    if abs(point1.x - point2.x) < Point.det:
        return (point1.x,)
    # normal line
    k = float(point1.y - point2.y) / (point1.x - point2.x)
    b = point1.y - k * point1.x
    return (k, b)


def get_center_line(square1, square2):
    """get a line split two square to equal size.

    return a line in the form of y = kx + b
    square is a dict has 4 keys indicate the 4 points. precisely,
    left, top, right, bottom
    point is a dict of 2 keys indicate the x and y value.
    for example, square.top.x means the top point's x value
    """
    c1 = get_square_center(square1)
    c2 = get_square_center(square2)
    # c1 == c2
    if c1.x == c2.x and c1.y == c2.y:
        c1.x = square1.left.x
        c1.y = square1.left.y
        c2.x = square1.right.x
        c2.y = square1.right.y
    return get_line(c1, c2)
