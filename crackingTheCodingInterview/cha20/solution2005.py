#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
You have a large text file containing words. Given any two words, find
the shortest distance (in terms of number of words) between them in
the file. Can you make the searching operation in O(1) time? What
about the space complexity for your solution?
"""

import bisect


def get_min_distance(large_string):
    # O(1) need cache, we can calculate all words min distance and
    # directly read, need O(n*n) space
    # or we can implement O(m*m) algorithm, where m is max count
    # of a word in the large_string, need O(n) space
    __cache = {}
    arr = large_string.split()
    for index, word in enumerate(arr):
        if __cache.get(word):
            bisect.insort(__cache[word], index)
        else:
            __cache[word] = [index]
    def _get_min_distance(word1, word2):
        if not __cache.get(word1) or not __cache.get(word2):
            return
        min_dis = abs(__cache[word1][0] - __cache[word2][0])
        for pos1 in __cache[word1]:
            for pos2 in __cache[word2]:
                dis = abs(pos1 - pos2)
                if dis < min_dis:
                    min_dis = dis
        return min_dis
    return _get_min_distance


if __name__ == '__main__':
    s = 'hello stranger where am i'
    h = get_min_distance(s)
    print h('hello', 'i')
