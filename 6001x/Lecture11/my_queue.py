# !/usr/bin/python
# -*- coding: utf-8 -*-

class Queue(object):
    def __init__(self):
        self.vals = []

    def insert(self, val):
        self.vals.append(val)

    def remove(self):
        try:
            return self.vals.pop(0)
        except IndexError:
            raise ValueError
