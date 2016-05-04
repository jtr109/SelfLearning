# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def creat_num(number):
    st = set()
    for n in range(1, number + 1):
        st.add(random.randint(0, 9))
    return st


def creat_set():
    number = random.randint(1, 10)
    st = creat_num(number)
    return st


def menu():
    a = creat_set()
    b = creat_set()
    print "set A is: %r.\nset B is: %r." % (a, b)
    aob = a | b
    anb = a & b
    print "A|B is %r.\nA&B is: %r" % (aob, anb)


if __name__ == '__main__':
    menu()
