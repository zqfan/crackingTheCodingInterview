#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha19.solution1911 import *


class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual([], get_all_pairs(3, []))

    def test_zero_sum(self):
        self.assertEqual([(-1, 1)],
                         get_all_pairs(0, [0, -1, 1]))

    def test_know_value(self):
        expected_result = set([(-2, 14), (-1, 13), (3, 9), (5, 7)])
        result = set(get_all_pairs(12,
                                   [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14])
                     )
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
