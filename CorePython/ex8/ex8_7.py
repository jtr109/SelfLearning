# !/usr/bin/env python
# -*- coding: utf-8 -*-

from ex8_5 import getfactors


def isperfect(num):
    fac = getfactors(num)
    fac.pop()
    sum1 = sum(fac)
    if sum1 == num:
        ret = True
    else:
        ret = False
    return ret


def menu():
    num = int(raw_input("Enter the number: "))
    print isperfect(num)


if __name__ == '__main__':
    menu()
