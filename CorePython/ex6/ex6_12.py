# !/usr/bin/env python
# -*- coding: utf-8 -*-


def findchr(s, c):
    len_c = len(c)
    len_s = len(s)
    for i in range(0, len_s):
        if c[0] == s[i] and c == s[i: (i + len_c)]:
            return i
    else:
        return -1

'''
# test
print(findchr('abcdefg', 'bc'))
print(findchr('abcdefg', 'cde'))
print(findchr('abcdefg', 'df'))
print(findchr('abcdefg', 'g'))
'''
