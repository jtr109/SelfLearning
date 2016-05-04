# !/usr/bin/env python
# -*- coding: utf-8 -*-


def my_pop(li, n=None):
    if n is None:
        n = len(li) - 1
    print li[n]
    new_list = li[:n] + li[n+1:]
    print new_list

my_pop(['a', 'b', 'c', 'd', 'e'], 0)
my_pop(['a', 'b', 'c', 'd', 'e'], 2)
my_pop(['a', 'b', 'c', 'd', 'e'], 4)
my_pop(['a', 'b', 'c', 'd', 'e'])