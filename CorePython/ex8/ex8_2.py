# !/usr/bin/env python
# -*- coding: utf-8 -*-


def out(f, t, i):
    ret = []
    x = f
    while x <= t:
        ret.append(x)
        x += i
    return ret


def menu():
    f = int(raw_input("from: "))
    t = int(raw_input("to: "))
    i = int(raw_input("increment: "))
    print out(f, t, i)


if __name__ == '__main__':
    menu()
