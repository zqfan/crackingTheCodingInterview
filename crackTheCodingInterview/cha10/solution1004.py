#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Write a method to implement *, - , / operations. You should use only
the + operator.

Analyze:
* only support integer operations
* the / will return a integer with floor(a/b)
"""

class NotIntegerError(Exception): pass
class InvalidOperatorError(Exception): pass
class DivideZeroError(Exception): pass

def arithmetic(operator, lhs, rhs):
    """return lhs operator rhs, i.e. 1 * 2

    raise NotIntegerError if any operand is not integer
    raise InvalidOperatorError if operator is not in *, /, -
    raise DivideZeroError if operator is / and rhs is 0
    """
    if not all((isinstance(lhs, int), isinstance(rhs, int))):
        raise NotIntegerError()
    if not operator in ('*', '/', '-'):
        raise InvalidOperatorError()
    if operator == '/' and rhs == 0:
        raise DivideZeroError()

    def _reverse(operand):
        if operand == 0:
            return 0
        step = 1 if operand < 0 else -1
        r = 0
        while operand:
            r = r + step
            operand = operand + step
        return r

    def _abs(operand):
        return operand if operand >= 0 else _reverse(operand)

    def multiply(lhs, rhs):
        if rhs == 0:
            return 0
        r = i = 0
        tlhs = lhs if lhs > 0 else _reverse(lhs)
        trhs = rhs if rhs > 0 else _reverse(rhs)
        if tlhs < trhs:
            return multiply(rhs, lhs)
        while i < trhs:
            r = r + tlhs
            i = i + 1
        if (lhs > 0 and rhs > 0) or (lhs < 0 and rhs < 0):
            return r
        else:
            return _reverse(r)

    def minus(lhs, rhs):
        rhs = multiply(rhs, -1)
        return lhs + rhs

    # -5/4 = -2 because python does
    def divide(lhs, rhs):
        if lhs == 0:
            return 0
        if rhs == 1:
            return lhs
        i = 0
        tlhs = lhs if lhs > 0 else _reverse(lhs)
        trhs = rhs if rhs > 0 else _reverse(rhs)
        while tlhs >= trhs:
            i = i + 1
            tlhs = minus(tlhs, trhs)
        if (lhs > 0 and rhs > 0) or (lhs < 0 and rhs < 0):
            return i
        else:
            return _reverse(i) if tlhs == 0 else _reverse(i + 1)

    opmap = {'*': multiply,
             '-': minus,
             '/': divide
             }

    return opmap[operator](lhs, rhs)
