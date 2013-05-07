#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
The Game of Master Mind is played as follows:
The computer has four slots containing balls that are red (R), yellow
(Y), green (G) or blue (B). For example, the computer might have RGGB
(e.g., Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).
You, the user, are trying to guess the solution. You might, for
example, guess YRGB.
When you guess the correct color for the correct slot, you get a
“hit”. If you guess a color that exists but is in the wrong slot, you
get a “pseudo-hit”. For example, the guess YRGB has 2 hits and one
pseudo hit.
For each guess, you are told the number of hits and pseudo-hits.
Write a method that, given a guess and a solution, returns the number
of hits and pseudo hits.
"""

def get_hits_and_pseudo(guess, solution):
    hit, pseudo = 0, []
    for i in range(4):
        if guess[i] in solution:
            # GGGG get 1 pseudo in RYGB
            if pseudo.count(guess[i]) < solution.count(guess[i]):
                pseudo.append(guess[i])
        if guess[i] == solution[i]:
            hit += 1
    # YRGB get 2 hits and 1 pseudo in RGGB
    return (hit, len(pseudo) - hit)
