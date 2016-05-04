# !/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)

if __name__ == '__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
