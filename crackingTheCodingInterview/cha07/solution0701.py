#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Design the data structures for a generic deck of cards. Explain how you would subclass it to implement particular card games.
"""

class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __eq__(self, card):
        return self.value == card.value and self.suit == card.suit

    def __gt__(self, card):
        if self.suit > card.suit:
            return True
        elif self.suit == card.suit:
            return self.value > card.value
        else:
            return False


