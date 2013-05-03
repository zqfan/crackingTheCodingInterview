#! /usr/bin/env python
# -*- coding: utf-8 -*-

class SetOfStack(object):
    stacks = []
    capacity = 10
    cur_stack = -1
    cur_index = capacity

    def push(self, data):
        if self.cur_index >= self.capacity - 1:
            self.stacks.append([data])
            self.cur_stack += 1
            self.cur_index = 0
        else:
            self.stacks[self.cur_stack].append(data)
            self.cur_index += 1

    def pop(self):
        if self.cur_stack < 0:
            return None
        data = self.stacks[self.cur_stack].pop()
        if self.cur_index <= 0:
            self.cur_index = self.capacity
            del self.stacks[self.cur_stack]
            self.cur_stack -= 1
        self.cur_index -= 1
        return data

    def popAt(self, index):
        if index < 0 or index > self.cur_stack:
            return None
        if index == self.cur_stack:
            return self.pop()
        
        data = self.stacks[index].pop()
        for i in range(index, len(self.stacks)-1):
            self.stacks[i].append(self.stacks[i+1][0])
            del self.stacks[i+1][0]
        if len(self.stacks[self.cur_stack]) == 0:
            del self.stacks[self.cur_stack]
            self.cur_stack -= 1
            self.cur_index = self.capacity - 1
        else:
            self.cur_index -= 1
        return data

def test():
    sos = SetOfStack()
    for i in range(1,15):
        sos.push(i)
    for i in range(1,16):
        print sos.stacks
        sos.popAt(0)


if __name__ == "__main__":
    test()
