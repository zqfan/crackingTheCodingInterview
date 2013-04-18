#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program to sort a stack in ascending order. You should not make any assump-
tions about how the stack is implemented. The following are the only functions that
should be used to write this program: push | pop | peek | isEmpty.
"""

import stack

def sort_stack(s):
    tmp_stack = stack.Stack()
    while not s.isEmpty():
        top_element = s.pop()
        while (not tmp_stack.isEmpty()) and tmp_stack.peek() > top_element:
            s.push(tmp_stack.pop())
        tmp_stack.push(top_element)
    return tmp_stack


def main():
    s = stack.Stack()
    s.push(2)
    s.push(1)
    s.push(3)
    s = sort_stack(s)
    print s.pop(), s.pop(), s.pop()


if __name__ == '__main__':
    main()
