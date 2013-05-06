#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
In Java, does the finally block gets executed if we insert a return
statement inside the try block of a try-catch-finally?

Analyze:
in java, if a try-catch-finally block has return statement in try
block, the finally block will be executed, unless the current thread
is killed by force.

in python, it is same as java, no matter what happen in try, else or catch
block, the statement in finally block will always be executed.
"""
