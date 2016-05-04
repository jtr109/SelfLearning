# !/usr/bin/env python
# -*- coding: utf-8 -*-

from ex8_4 import isprime
from ex8_5 import getfactors


def factor(num):
    if isprime(num):
        return [1, num]
    else:
        num1 = num
        factors = []
        while num1 > 1:
            g = getfactors(num1)
            g1 = g[1]
            factors.append(g1)
            num1 /= g1
        return factors


def menu():
    num = int(raw_input("Enter the number: "))
    print factor(num)


if __name__ == '__main__':
    menu()
