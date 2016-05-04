# !/usr/bin/env python
# -*- coding: utf-8 -*-


def fb(n):
    if n == 1:
        res = 1
    elif n == 2:
        res = 2
    else:
        res = fb(n-1) + fb(n-2)
    return res


def main():
    for n in range(1, 40):
        print "fb(%d) = %d" % (n, fb(n))


if __name__ == '__main__':
    main()