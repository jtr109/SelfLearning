# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    Ln = s.split('.')
    m = reduce(lambda x, y: 10 * x + y, map(char2num, Ln[0]))
    n = reduce(lambda x, y: 0.1 * x + y, map(char2num, reversed(Ln[1])))
    return m + 0.1 * n

print('str2float(\'123.456\') =', str2float('123.456'))
print(123.456 == str2float('123.456'))