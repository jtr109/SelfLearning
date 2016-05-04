# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def fac_iterate(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


def fac_reduce(n):
    ret = reduce((lambda x, y: x * y), range(1, n+1))
    return ret


def fac_recurse(n):
    if n == 1:
        ret = 1
    else:
        ret = n * fac_recurse(n-1)
    return ret


def timeit(func, n):
    start_time = time.time()
    retval = func(n)
    finish_time = time.time()
    sp_time = finish_time - start_time
    result = (retval, sp_time)
    return result


def main():
    funcs = (fac_iterate, fac_reduce, fac_recurse)
    n = int(raw_input("N = "))
    for eachFunc in funcs:
        print '_' * 20
        result = timeit(eachFunc, n)
        print "%2d!\tCost: %r(s)" % (n, result[1])


if __name__ == '__main__':
    main()
