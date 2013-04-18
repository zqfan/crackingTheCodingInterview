#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import os
import sys
import unittest
import random


TEST_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_ROOT_DIR = os.path.dirname(TEST_FILE_DIR)
SOURCE_ROOT_DIR = os.path.dirname(TEST_ROOT_DIR)
print SOURCE_ROOT_DIR
sys.path.append(SOURCE_ROOT_DIR)
from cha10.solution1003 import is_intersect


class CTCI1003Test(unittest.TestCase):
    def test_one_base_point(self):
        """base point should return false"""
        line1, line2 = (0, 0, 0), (1, 2, 3)
        self.assertFalse(is_intersect(line1, line2))

    def test_two_base_points(self):
        """base point should return false"""
        line1 = (0, 0, 0)
        self.assertFalse(is_intersect(line1, line1))

    def test_single_vertical_line(self):
        """single vertical line should return true"""
        line1 = (random.randint(1, 65535), 0,
                 random.randint(0, 65535))
        self.assertTrue(is_intersect(line1, line1))

    def test_two_different_vertical_lines(self):
        """two different vertical lines should return false"""
        a1, c1, a2, c2 = (random.randint(1, 65535),
                          random.randint(0, 65535),
                          random.randint(1, 65535),
                          random.randint(0, 65535))
        if a1 * c2 == a2 * c1:
            c2 += 1
        line1, line2 = (a1, 0, c1), (a2, 0, c2)
        self.assertFalse(is_intersect(line1, line2))

    def test_single_horizon_line(self):
        """single horizon line should return true"""
        line1 = (0, random.randint(1, 65535),
                 random.randint(0, 65535))
        self.assertTrue(is_intersect(line1, line1))

    def test_two_different_horizon_lines(self):
        b1, c1, b2, c2 = (random.randint(1, 65535),
                          random.randint(0, 65535),
                          random.randint(1, 65535),
                          random.randint(0, 65535))
        if b1 * c2 == b2 * c1:
            c2 += 1
        line1, line2 = (0, b1, c1), (0, b2, c2)
        self.assertFalse(is_intersect(line1, line2))

    def test_single_slash(self):
        line1 = (random.randint(1, 65535),
                 random.randint(1, 65535),
                 random.randint(0, 65535))
        self.assertTrue(is_intersect(line1, line1))

    def test_two_different_intersected_slashes(self):
        a1, b1, c1 = (random.randint(1, 65535),
                      random.randint(1, 65535),
                      random.randint(0, 65535))
        a2, b2, c2 = (random.randint(1, 65535),
                      random.randint(1, 65535),
                      random.randint(0, 65535))
        if a1 * b2 == b1 * a2:
            b2 += 1
        line1, line2 = (a1, b1, c1), (a2, b2, c2)
        self.assertTrue(is_intersect(line1, line2))

    def test_two_different_parallel_slashes(self):
        a1, b1, c1 = (random.randint(1, 65535),
                      random.randint(1, 65535),
                      random.randint(0, 65535))
        c2 = random.randint(1,65535) + c1
        line1, line2 = (a1, b1, c1), (a1, b1, c2)
        self.assertFalse(is_intersect(line1, line2))

if __name__ == '__main__':
    unittest.main()
