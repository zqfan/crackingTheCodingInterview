#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Crack the Coding Interview

There are three ants on different vertices of a triangle. What is the
probability of collision (between any two or all of them) if they
start walking on the sides of the triangle? Similarly find the
probability of collision with ‘n’ ants on an ‘n’ vertex polygon.

Analyze:
for each ant, it has two direction to go, the there are 2^n cases.
only two of them will avoid collision: the same direction for all of
the ants. then the answer is (2^n - 2)/2^n = 1 - 1/2^(n-1).
"""
