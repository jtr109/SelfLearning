# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def timeit(func, *nkwargs, **kwargs):
    time.clock()
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return time.clock()


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            print '%s(%s)= ' % (eachFunc.__name__, 'eachVal'), retval



if __name__ == '__main__':
    test()
