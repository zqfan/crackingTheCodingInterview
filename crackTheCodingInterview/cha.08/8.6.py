#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=4 shiftwidth=4

"""
8.6
Implement the “paint fill” function that one might see on many image
editing programs. That is, given a screen (represented by a 2
dimensional array of Colors), a point, and a new color, fill in the
surrounding area until you hit a border of that color.’
"""

def paint_fill(screen, x, y, color):
    """Paint fill the block with the color.

    A block is defined as an area with exactly the same color as the
    point, and also contains the point. So a line may also fill as
    a area.
    """
    def _is_block(screen, x, y):
        """
        check if this point is in a block or just a line or cross.
        """
        return True

    def _in_screen(screen, x, y):
        if x < 0 or x >= len(screen):
            return False
        if y < 0 or y >= len(screen[0]):
            return False
        return True

    def _try_fill_pixel(screen, x, y, old_color, new_color):
        if not _in_screen(screen, x, y):
            return
        if screen[x][y] == old_color:
            screen[x][y] = new_color
            _try_fill_pixel(screen, x, y-1, old_color, new_color)
            _try_fill_pixel(screen, x+1, y, old_color, new_color)
            _try_fill_pixel(screen, x, y+1, old_color, new_color)
            _try_fill_pixel(screen, x-1, y, old_color, new_color)

    if not _in_screen(screen, x, y):
        return
    if not _is_block(screen, x, y):
        return
    old_color = screen[x][y]
    _try_fill_pixel(screen, x, y, old_color, color)
