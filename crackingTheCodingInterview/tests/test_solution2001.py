#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest
import random

from utils import *
patch_sys_path()
from cha20.solution2001 import *


class Test(unittest.TestCase):
    def test_zero(self):
        r = random.randint(1, 65535)
        self.assertEqual(0, add(0, 0))
        self.assertEqual(r, add(0, r))
        self.assertEqual(r, add(r, 0))

    def test_know_value(self):
        for i in range(128):
            r1 = random.randint(0, 65535)
            r2 = random.randint(0, 65535)
            self.assertEqual(r1 + r2, add(r1, r2))


if __name__ == '__main__':
    unittest.main()
