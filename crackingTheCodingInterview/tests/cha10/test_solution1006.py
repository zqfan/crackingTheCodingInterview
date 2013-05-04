#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha10.solution1006 import *


class Test(unittest.TestCase):
    def test_empty(self):
        r = get_most_points_line([])
        self.assertEqual(r, None)

    def test_single(self):
        r = get_most_points_line([Point(0, 0)])
        self.assertEqual(r, None)


if __name__ == '__main__':
    unittest.main()
