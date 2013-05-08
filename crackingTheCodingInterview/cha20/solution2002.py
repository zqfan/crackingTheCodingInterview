#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method to shuffle a deck of cards. It must be a perfect
shuffle - in other words, each 52! permutations of the deck has to be
equally likely. Assume that you are given a random number generator
which is perfect.
"""

import random


def get_shuffled_cards():
    cards = range(1, 53)
    for i in range(52):
        # select one card
        x = random.randint(i, 51)
        # remove it from source cards pile,
        # store it to target cards pile
        # [0, i] is current target pile, [i+1, 51] is remain source
        # pile
        cards[i], cards[x] = cards[x], cards[i]
    return cards
