#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha01.solution0101 import *


class Test(unittest.TestCase):
    def test_non_str(self):
        self.assertFalse(is_unique_str(123))
        self.assertFalse(is_unique_str(None))
        self.assertFalse(is_unique_str([]))

    def test_empty_str(self):
        self.assertTrue(is_unique_str(''))

    def test_unique_str(self):
        self.assertTrue(is_unique_str('world'))

    def test_duplicated_str(self):
        self.assertFalse(is_unique_str('hello'))


if __name__ == '__main__':
    unittest.main()
