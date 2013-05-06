#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest
import random

from utils import *
patch_sys_path()
from cha05.solution0503 import *


class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual((0, 0), neighbour(0))

    def test_normal_value(self):
        for i in range(128):
            n = random.randint(-65535, 65535)
            self.assertEqual(neighbour(n), neighbour_bf(n))


if __name__ == '__main__':
    unittest.main()
