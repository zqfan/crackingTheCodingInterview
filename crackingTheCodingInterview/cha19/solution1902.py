#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Design an algorithm to figure out if someone has won in a game of
tic-tac-toe.
"""

def get_winner(board):
    """Return if there is a winner of current board.

    @param: board It is a N*N matrix, each element will be None, 0 or
    1
    @return: if there is no winner, return None, else if there is a
    winner, return the winner, if there are two winner, return None
    """
    def get_color(i, j):
        if i < 0 or i >= len(board):
            return None
        if j < 0 or j >= len(board[0]):
            return None
        return board[i][j]

    def triple_piece(i, j):
        color = board[i][j]
        if not color:
            return False
        # row
        r = color == get_color(i, j+1)
        r = r and (color == get_color(i, j+2))
        # col
        c = color == get_color(i+1, j)
        c = c and (color == get_color(i+2, j))
        # diagonal
        d = color == get_color(i+1, j+1)
        d = d and (color == get_color(i+2, j+2))
        return r or c or d

    winner = None
    winner_count = 0
    # scan from left to right, from top to bottom
    for i in range(len(board)):
        for j in range(len(board[0])):
            if triple_piece(i, j):
                if not winner:
                    winner = board[i][j]
                    winner_count = 1
                elif winner != board[i][j]:
                    winner_count = 2
    return winner if winner_count == 1 else None
