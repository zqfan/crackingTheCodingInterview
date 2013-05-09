#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Given two words of equal length that are in a dictionary, write a
method to transform one word into another word by changing only one
letter at a time. The new word you get in each step must be in the
dictionary.
EXAMPLE:
Input: DAMP, LIKE
Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE
"""

def get_transfer_steps(word1, word2, dictionary):
    """
    according from the question:
    assume dictionary is a list, all words are upper case, word1 and
    word2 are not none and in dictionary, so there is no check needed
    """
    bfs_queue = [(word1, [])]
    while len(bfs_queue):
        cur = bfs_queue[0]
        word, transform = cur[0], cur[1][:]
        del bfs_queue[0]
        for i in range(len(word)):
            for j in range(0, 26):
                if ord('A') + j != ord(word[i]):
                    new_word = word[:i] + chr(ord('A')+j) + word[i+1:]
                    if (new_word in transform or
                        new_word not in dictionary):
                        continue
                    transform.append(word)
                    if new_word == word2:
                        transform.append(word2)
                        return transform
                    bfs_queue.append((new_word, transform))

def print_transfer_steps(word1, word2):
    word_dict = ['DAMP', 'LAMP', 'LIMP', 'LIME', 'LIKE']
    if not word1 or not word2:
        return
    if not len(word1) == len(word2):
        return
    if not word1 in word_dict or not word2 in word_dict:
        return
    if word1 == word2:
        print word1
        return
    steps = get_transfer_steps(word1, word2, word_dict)
    for step in steps[:-2]:
        print step, ' -> ', 
    print steps[-1]

if __name__ == '__main__':
    print_transfer_steps('DAMP', 'DAMP')
    print_transfer_steps('DAMP', 'LIKE')
