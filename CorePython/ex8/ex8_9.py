# !/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    a = 1
    b = 0
    ret = 0
    for i in range(1, n + 1):
        ret = a + b
        a = b
        b = ret
    return ret


def menu():
    n = int(raw_input("Enter the N: "))
    print "fib(%d) is: %d" % (n, fib(n))


if __name__ == '__main__':
    menu()
