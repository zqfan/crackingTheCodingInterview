#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""
Imagine you have a call center with three levels of employees: fresher, technical lead (TL), product manager (PM). There can be multiple employees, but only one TL or PM. An incoming telephone call must be allocated to a fresher who is free. If a fresher can’t handle the call, he or she must escalate the call to technical lead. If the TL is not free or not able to handle it, then the call should be escalated to PM. Design the classes and data structures for this problem. Implement a method getCallHandler().
"""

import random
import time


class Employee(object):
    """Basic employee class"""
    def __init__(self, id, name, level=0):
        self.id = id
        self.name = name
        self.level = level
        self.free = True

    def can_handle_call(self, call):
        """if this employee can handle the call"""
        return self.free and self.level >= call.difficulty

    def handle_call(self, call):
        """Handle the call."""
        self.free = False
        res = '0' * random.randint(0, 65535)
        time.sleep(random.randint(1,10))
        call.get_response(res)
        self.free = True


class Fresher(Employee):
    def __init__(self, id, name):
        super(Fresher, self).__init__(id, name, 1)


class TechnicalLead(Employee):
    def __init__(self, id, name):
        super(TechnicalLead, self).__init__(id, name, 2)


class ProductManager(Employee):
    def __init__(self, id, name):
        super(ProductManager, self).__init__(id, name, 3)


class CallHandler(object):
    def __init__(self):
        self.freshers = []
        for i in range(10):
            self.freshers.append(Fresher(i, str(i)))
        self.technical_leader = TechnicalLeader(11, str(11))
        self.product_manager = ProductManager(12, str(12))

    def getCallHandler(call):
        """Get call handler"""
        for fresher in self.freshers:
            if fresher.can_handle_call(call):
                return fresher
        if self.technical_leader.can_handle_call(call):
            return self.technical_leader
        if self.product_manager.can_handle_call(call):
            return self.product_manager

    def handle_call(call):
        while True:
            call_handler = self.getCallHandler(call)
            if not call_handler:
                time.sleep(3)
            else:
                break
        call_hander.handle_call(call)


class Call(object):
    def __init__(self, difficulty=0, content=''):
        self.difficulty = difficulty
        self.__content = content
        self.__completed = False

    def get_response(self, response):
        if self.__satisfy(response):
            self.__completed = True

    def is_completed(self):
        return self.__completed

    def __satisfy(self, response):
        if len(response) > len(self.__content):
            return True