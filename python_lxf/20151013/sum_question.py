# !/usr/bin/env python3
# -*- coding: utf-8 -*-

sum = 0
n = input('1 + 2 + ... + ')
x = int(n)
for i in range(x + 1):
    sum += i
print('= %d' % sum)
