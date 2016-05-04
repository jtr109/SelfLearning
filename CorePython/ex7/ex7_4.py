# !/usr/bin/env python
# -*- coding: utf-8 -*-


def dict_zip(list1, list2):
    new_dict = dict(zip(list1, list2))
    return new_dict

'''
list1 = [1, 2, 3]
list2 = ['abc', 'def', 'ghi']
print dict_zip(list1, list2)
'''
