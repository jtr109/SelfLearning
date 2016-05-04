# !/usr/bin/env python
# -*- coding: utf-8 -*-

def up_side_down(dict1):
    dict2 = {}
    keys1 = dict1.keys()
    for key in keys1:
        value = dict1[key]
        dict2[value] = key
    return dict2

'''
a = {1: 'a', (2, 3): 'c, d, e', '2': (1,3,4)}
b = up_side_down(a)
c = up_side_down(b)

print b
print c
'''
