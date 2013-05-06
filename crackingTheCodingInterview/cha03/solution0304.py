#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
In the classic problem of the Towers of Hanoi, you have 3 rods and N
disks of different sizes which can slide onto any tower. The puzzle
starts with disks sorted in ascending order of size from top to bottom
(e.g., each disk sits on top of an even larger one). You have the
following constraints:
(A) Only one disk can be moved at a time.
(B) A disk is slid off the top of one rod onto the next rod.
(C) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first rod to the last using
Stacks.
"""

import stack

def hanoi_v1(n, start_rod, target_rod, tmp_rod):
    if n < 1:
        return
    if n == 1:
        print 'move disk 1 from rod %d to rod %d' % (start_rod,
                                                     target_rod)
        return
    hanoi_v1(n-1, start_rod, tmp_rod, target_rod)
    print 'move disk %d from rod %d to rod %d' % (n, start_rod,
                                                  target_rod)
    hanoi_v1(n-1, tmp_rod, target_rod, start_rod)

def hanoi(n):
    """print hanoi steps using stacks.

    当盘子的个数为n时，移动的次数应等于2^n – 1。
    后来一位美国学者发现一种出人意料的简单方法，只要轮流进行两步操作就可以
    了。首先把三根柱子按顺序排成品字型，把所有的圆盘按从大到小的顺序放在柱
    子A上，根据圆盘的数量确定柱子的排放顺序：若n为偶数，按顺时针方向依次摆
    放 A B C；

    若n为奇数，按顺时针方向依次摆放 A C B。
    （1）按顺时针方向把圆盘1从现在的柱子移动到下一根柱子，即当n为偶数时，
    若圆盘1在柱子A，则把它移动到B；若圆盘1在柱子B，则把它移动到C；若圆盘1
    在柱子C，则把它移动到A。
    （2）接着，把另外两根柱子上可以移动的圆盘移动到新的柱子上。即把非空柱
    子上的圆盘移动到空柱子上，当两根柱子都非空时，移动较小的圆盘。这一步没
    有明确规定移动哪个圆盘，你可能以为会有多种可能性，其实不然，可实施的行
    动是唯一的。
    （3）反复进行（1）（2）操作，最后就能按规定完成汉诺塔的移动。
    """
    if n < 0:
        return
    rods = [stack.Stack(), stack.Stack(), stack.Stack()]
    for i in range(n):
        rods[0].push(n-i)
    if n % 2 == 1:
        order = [2, 0, 1]
    else:
        order = [1, 2, 0]
    # need 2^n - 1 steps
    for i in range(2**n - 1):
        if i % 2 == 0:
            for j in range(3):
                if rods[j].peek() == 1:
                    rods[j].pop()
                    rods[order[j]].push(1)
                    print 'move disk 1 from %d to %d' % (j + 1,
                                                         order[j] + 1)
                    break
        else:
            d = []
            for j in range(3):
                if rods[j].peek() != 1:
                    d.append((j, rods[j].peek()))
            # Move the small one to the bigger one
            # Note that: None < anything
            if (not d[0][1]) or (d[1][1] and d[0][1] > d[1][1]):
                rods[d[1][0]].pop()
                rods[d[0][0]].push(d[1][1])
                print 'move disk %d from %d to %d' % (d[1][1],
                                                      d[1][0] + 1,
                                                      d[0][0] + 1)
            else:
                rods[d[0][0]].pop()
                rods[d[1][0]].push(d[0][1])
                print 'move disk %d from %d to %d' % (d[0][1],
                                                      d[0][0] + 1,
                                                      d[1][0] + 1)
