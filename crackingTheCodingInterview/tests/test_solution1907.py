#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha19.solution1907 import *


class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(0, max_sum_continuous_sequence([]))

    def test_all_negative(self):
        self.assertEqual(-1, max_sum_continuous_sequence(
                [-10, -2, -3, -4, -1, -9]))

    def test_all_zero(self):
        self.assertEqual(0, max_sum_continuous_sequence([0, 0, 0]))

    def test_know_value(self):
        self.assertEqual(5, max_sum_continuous_sequence(
                [2, -8, 3, -2, 4, -10]))


if __name__ == '__main__':
    unittest.main()
