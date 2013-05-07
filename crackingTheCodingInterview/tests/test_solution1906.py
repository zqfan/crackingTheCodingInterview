#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest

from utils import *
patch_sys_path()
from cha19.solution1906 import *


class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual('Zero', eng_phrase(0))

    def test_single(self):
        self.assertEqual('One', eng_phrase(1))
        self.assertEqual('Nine', eng_phrase(9))

    def test_teens(self):
        self.assertEqual('Twelve', eng_phrase(12))

    def test_xtys(self):
        self.assertEqual('Thirty', eng_phrase(30))

    def test_hundred(self):
        self.assertEqual('Four Hundred and Fifty Six',
                         eng_phrase(456))

    def test_thousand(self):
        self.assertEqual('Nine Hundred and Ninety Nine Thousand',
                         eng_phrase(999000))
        self.assertEqual('%s%s' % (
                'Nine Hundred and Ninety Nine Thousand, ',
                'Nine Hundred and Ninety Nine'), eng_phrase(999999))


if __name__ == '__main__':
    unittest.main()
