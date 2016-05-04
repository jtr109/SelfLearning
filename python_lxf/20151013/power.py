# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

x_s = input('x = ')
n_s = input('n = ')
x = int(x_s)
n = int(n_s)

s = power(x, n)
print('%d ^ %d = %d' % (x, n, s))
