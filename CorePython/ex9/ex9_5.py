# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve
import random


def score_update(sub):
    di = r'C:\Programs\CorePython\ex9\tmp\\'[:-1]
    path = ''.join([di, sub, '.txt'])
    sh = shelve.open(path)
    sh.clear()
    sh['Tom'] = (sub, random.randint(50, 100))
    sh['Jack'] = (sub, random.randint(50, 100))
    sh['Lucy'] = (sub, random.randint(50, 100))
    sh['Helen'] = (sub, random.randint(50, 100))
    sh['Dick'] = (sub, random.randint(50, 100))
    sh.close()


def show_all(path):
    pass


def add_item(path):
    pass


def del_item(path):
    pass

'''
score_update('English')
score_update('Math')
score_update('Chinese')
'''

