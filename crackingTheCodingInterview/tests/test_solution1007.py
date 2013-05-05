#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha10.solution1007 import *


class Test(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(0, f(-1))

    def test_zero(self):
        self.assertEqual(0, f(0))

    def test_first(self):
        self.assertEqual(1, f(1))

    def test_know_value(self):
        self.assertEqual(3, f(2))
        self.assertEqual(5, f(3))
        self.assertEqual(7, f(4))
        self.assertEqual(9, f(5))
        self.assertEqual(63, f(13))
        self.assertEqual(75, f(14))


if __name__ == '__main__':
    unittest.main()
