#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha19.solution1910 import *


class Test(unittest.TestCase):
    def test_range(self):
        for i in range(128):
            x = rand7()
            self.assertTrue(x in range(1, 8))


if __name__ == '__main__':
    unittest.main()
