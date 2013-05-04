#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import unittest
import random

import utils
utils.patch_sys_path()
from cha10.solution1004 import *


class CTCI1004Test(unittest.TestCase):
    def test_non_integer(self):
        operator, lhs, rhs = '*', '1', 0.3
        self.assertRaises(NotIntegerError,
                         arithmetic,
                         *(operator, lhs, rhs))

    def test_invalid_operator(self):
        operator, lhs, rhs = '%', 1, 2
        self.assertRaises(InvalidOperatorError,
                          arithmetic,
                          *(operator, lhs, rhs))

    def test_multiply_zero(self):
        self.assertEqual(0, arithmetic('*', 0, 0))
        for i in range(128):
            lhs, rhs = 0, random.randint(-1024, 1024)
            self.assertEqual(0, arithmetic('*', lhs, rhs))
            lhs, rhs = random.randint(-1024, 1024), 0
            self.assertEqual(0, arithmetic('*', lhs, rhs))

    def test_multiply_operation(self):
        for i in range(128):
            lhs = random.randint(-1024, 1024)
            rhs = random.randint(-1024, 1024)
            self.assertEqual(lhs * rhs, arithmetic('*', lhs, rhs))

    def test_minus_operation(self):
        for i in range(128):
            lhs = random.randint(-1024, 1024)
            rhs = random.randint(-1024, 1024)
            self.assertEqual(lhs - rhs, arithmetic('-', lhs, rhs))

    def test_divide_zero(self):
        for i in range(128):
            lhs = random.randint(-1024, 1024)
            self.assertRaises(DivideZeroError,
                              arithmetic,
                              *('/', lhs, 0))

    def test_zero_divide(self):
        for i in range(128):
            rhs = random.randint(-1024, 1024)
            rhs = rhs if rhs !=0 else 1
            self.assertEqual(0, arithmetic('/', 0, rhs))

    def test_divide_operation(self):
        for i in range(128):
            lhs = random.randint(-1024, 1024)
            rhs = random.randint(-1024, 1024)
            rhs = rhs if rhs != 0 else 1
            self.assertEqual(lhs / rhs, arithmetic('/', lhs, rhs))


if __name__ == '__main__':
    unittest.main()
