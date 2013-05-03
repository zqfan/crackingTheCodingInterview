#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.8
Write an algorithm to print all ways of arranging eight queens on a
chess board so that none of them share the same row, column or
diagonal.
"""

def eight_queens():
    def _place(n, location):
        if n == 8:
            for l in location:
                print l,
            print
            return 1
        count = 0
        post = []
        for l in location:
            post.append(l[1])
            post.append(l[1] - l[0] + n)
            post.append(l[1] + l[0] - n)
        for i in range(8):
            if i in post:
                continue
            lc = location[:]
            lc.append([n,i])
            count += _place(n+1, lc)
        return count

    print "total %d" %  _place(0, [])


if __name__ == "__main__":
    eight_queens()
