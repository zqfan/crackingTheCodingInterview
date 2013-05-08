#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest
import random

from utils import *
patch_sys_path()
from cha20.solution2004 import *


class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(0, get_digit_count(0))

    def test_negative(self):
        for i in range(128):
            r = random.randint(-65535, -1)
            self.assertEqual(get_digit_count(r), get_digit_count(-r))

    def test_know_value(self):
        self.assertEqual(1, get_digit_count(3))
        self.assertEqual(2, get_digit_count(12))
        self.assertEqual(69, get_digit_count(222))


if __name__ == '__main__':
    unittest.main()
