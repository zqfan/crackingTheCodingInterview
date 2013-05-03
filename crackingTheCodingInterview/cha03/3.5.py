#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue(object):
    def __init__(self):
        self.main = []
        self.swap = []

    def enqueue(self, data):
        for i in range(0,len(self.main)):
            self.swap.append(self.main.pop())
        self.main.append(data)
        for i in range(0,len(self.swap)):
            self.main.append(self.swap.pop())

    def dequeue(self):
        return self.main.pop()


def test():
    mq = MyQueue()
    for i in range(1,10):
        mq.enqueue(i)
    for i in range(1,10):
        print mq.dequeue()


if __name__ == "__main__":
    test()
