# !/usr/bin/env python
# -*- coding: utf-8 -*-


def getfactors(num):
    factors = [x for x in range(1, num+1) if num % x == 0]
    return factors


def menu():
    num = int(raw_input("Enter the number: "))
    print getfactors(num)


if __name__ == '__main__':
    menu()
