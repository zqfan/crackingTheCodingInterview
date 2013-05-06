#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Design a chess game using object oriented principles.

Chinese chess game
"""

import random
import time


class Board(object):
    """Board record current state"""
    def __init__(self):
        self.__chess_pieces = self.init_chess_pieces()
        self.pos = [None for i in range(90)]
        self.__winner = None # 0 for black, 1 for red
        self.__turn = random.randint(0, 2) # 0 for black, 1 for red
        self.__players = []

    def set_player(self, player1, player2):
        self.__players = [player1, player2]

    def start(self):
        while not self.__winner:
            self.__players[self.turn].get_turn()

    def init_chess_pieces(self):
        """initialize all chess pieces"""
        pass

    def get_chess_pieces(self):
        return tuple(self.__chess_pieces)

    def move(self, piece_index, pos):
        # wrong index
        if piece_index < 0 or len(self.__chess_pieces) <= piece_index:
            return
        piece = self.__chess_pieces[piece_index]
        # move the wrong piece
        if not piece.color == self.turn:
            return
        # wrong pos
        if not piece.can_move_to(pos):
            return
        # delete the piece of pos
        if self.pos[pos]:
            del self.__chess_pieces[self.pos[pos]]
        # move the piece to pos
        self.pos[pos] = piece_index
        self.pos[piece.pos] = None
        self.turn = 1 - self.turn


class Player(object):
    def __init__(self, board):
        self.board = board

    def get_turn(self, pieces):
        pieces = self.board.get_chess_pieces()
        # calculate then decide
        time.sleep(random.randint(0,30))
        piece_index = random.randint(0, len(pieces))
        pos = random.randint(0, 9) * 10 + random.randint(0, 10)
        self.board.move(piece_index, pos)


class ComputePlayer(Player):
    def __init__(self, diffcult):
        pass


class HumanPlayer(Player):
    pass


class Piece(object):
    def __init__(self, color, value, pos):
        pass

    def can_move_to(self, pos):
        pass
