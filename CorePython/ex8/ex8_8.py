# !/usr/bin/env python
# -*- coding: utf-8 -*-


def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac


def menu():
    n = int(raw_input("N = "))
    fac = factorial(n)
    print "%d! = %d" % (n, fac)


if __name__ == '__main__':
    menu()
