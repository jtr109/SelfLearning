# !/usr/bin/python
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    n = s.find('.')
    new_s = s[:n] + s[n+1:]
    l = map(char2num, new_s)
    return reduce(lambda x, y: 10 * x + y, l) / 10.0 ** n

if __name__ == '__main__':
    print('str2float(\'123.456\') =', str2float('123.456'))
