#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
9.2
Write a method to sort an array of strings so that all the anagrams
are next to each other.
"""

def sort_anagram(arr):
    def anagram_cmp(x, y):
        xx = list(x)
        xx.sort()
        yy = list(y)
        yy.sort()
        return cmp(xx,yy)

    arr.sort(cmp=anagram_cmp)


if __name__ == "__main__":
    arr = ["anagram","has","ash","triangle","integral"]
    sort_anagram(arr)
    print arr
