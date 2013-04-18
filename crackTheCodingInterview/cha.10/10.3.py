#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given two lines on a Cartesian plane, determine whether the two lines
would intersect.

Analyze:
a1x + b1y + c1 = 0 (1)
a2x + b2y + c2 = 0 (2)
two lines are intersect because they have a share point. which means:
exists a (x0, y0) meets:
a1x0 + b1y0 + c1 = 0 (3)
a2x0 + b2y0 + c2 = 0 (4)

so if the two lines is actually one line, then they are intersect,
because for each point, (3) and (4) are right.

consider the slope of the two lines, if they are same, and if they are
two different lines, they will not intersect, if the slopes are
different, they will intersect, and the intersect point is:
oops, i forget the formula.... something like (3)*a2 - (4)*a1, then
you get x0 = ly0 + m, then put the x0 in any one of (3) or (4), then
you will get y0 and you can get x0 too.

let's see the code.
"""

def is_intersect(line1, line2):
    """Determine if the two lines are intersect.

    return true if line1 is line2
    line1 = (a1, b1, c1) which represents a1x + b1y + c1 = 0
                         a1, b1, c1 are all integer
    line2 = (a2, b2, c2) yes, you get it
    """
    if line1[1] * line2[1] == 0:
        if line1[1] + line2[1] == 0:
            pass
        else
