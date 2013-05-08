#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha20.solution2002 import *


class Test(unittest.TestCase):
    def test_shuffle(self):
        for i in range(128):
            r = get_shuffled_cards()
            r = list(set(r))
            self.assertEqual(range(1, 53), r)


if __name__ == '__main__':
    unittest.main()
