#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha10.solution1005 import *


class Test(unittest.TestCase):
    def test_same_square(self):
        s = Square(Point(-1, 1), Point(1, 1),
                   Point(1, -1), Point(-1, -1))
        r = get_center_line(s, s)
        self.assertEqual(r, (-1, 0))

    def test_vertical_line(self):
        s1 = Square(Point(-1, 0), Point(1, 0),
                    Point(1, -1), Point(-1, -1))
        s2 = Square(Point(-1, 1), Point(1, 1),
                    Point(1, 0), Point(-1, 0))
        r = get_center_line(s1, s2)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], 0)

    def test_horizon_line(self):
        s1 = Square(Point(-1, 1), Point(0, 1),
                    Point(0, 0), Point(-1, 0))
        s2 = Square(Point(0, 1), Point(1, 1),
                    Point(1, 0), Point(0, 0))
        r = get_center_line(s1, s2)
        self.assertEqual(r, (0, 0.5))


if __name__ == '__main__':
    unittest.main()
