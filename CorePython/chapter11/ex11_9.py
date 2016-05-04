# !/usr/bin/env python
# -*- coding: utf-8 -*-


def average(ls):
    n = float(len(ls))
    s = reduce((lambda x,y: x+y), ls)
    return s/n


def main():
    ls = range(1, 101)
    print average(ls)


if __name__ == '__main__':
    main()
