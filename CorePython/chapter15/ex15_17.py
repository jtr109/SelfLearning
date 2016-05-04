# !/usr/bin/python
# -*- coding: utf-8 -*-

import re


def chosen(n):
    try:
        redata = open('redata.txt', 'r')
        data = redata.readlines()
    finally:
        redata.close()
    return census(data, n)


def census(data, n):
    patt = '([A-Za-z]{3})\s([A-Za-z]{3}).+'
    ret = {}
    for d in data:
        print d,
        t = re.match(patt, d).group(n)
        try:
            ret[t] += 1
        except KeyError:
            ret[t] = 1
    return ret


if __name__ == '__main__':
    choice = raw_input('"date" or "month"?\n> ')
    if choice == 'date':
        c = chosen(1)
    elif choice == 'month':
        c = chosen(2)
    print c


