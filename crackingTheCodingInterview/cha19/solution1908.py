#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Design a method to find the frequency of occurrences of any given word
in a book.
"""

import re


def count(word, book):
    """Only handle ASCII string"""
    if not word or not book:
        return 0
    tmp_book = re.sub(r'[^a-zA-Z]', ' ', book).split()
    return book.count(word)


def count_with_cache(book):
    if not book:
        return
    cache = {}
    tmp_book = re.sub(r'[^a-zA-Z]', ' ', book).split()
    for word in tmp_book:
        if not cache.get(word):
            cache[word] = tmp_book.count(word)
    def count(word):
        r = cache.get(word)
        return r if r else 0
    return count
