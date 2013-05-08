#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a program to find the longest word made of other words.
"""

def get_longest_composite_word(words):
    """
    Although a long word may be made of many words, but in English
    sentence, composite word is usually made of two words. So i narrow
    down the problem.

    And a long word may connect two words by '-'
    """
    sorted_words = sorted(words, reverse=True)
    for index, word in enumerate(sorted_words):
        if word.find('-') != -1:
            split_words = word.split('-')
            if (len(split_words) == 2 and
                split_words[0] in sorted_words and
                split_words[1] in sorted_words):
                return word
        for i in range(len(word)):
            if word[:i] in sorted_words and word[i:] in sorted_words:
                return word


if __name__ == '__main__':
    print get_longest_composite_word(['heartbreak', 'heart', 'break',
                                      'ear'])
