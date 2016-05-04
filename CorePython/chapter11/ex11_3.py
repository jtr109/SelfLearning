# !/usr/bin/env python
# -*- coding: utf-8 -*-


def max2(a, b):
    if a > b:
        return a
    else:
        return b


def min2(a, b):
    if a < b:
        return a
    else:
        return b


def my_max(*argv):
    if len(argv) == 1:
        argv = argv[0]
    return reduce(max2, argv)


def my_min(*argv):
    if len(argv) == 1:
        argv = argv[0]
    return reduce(min2, argv)
