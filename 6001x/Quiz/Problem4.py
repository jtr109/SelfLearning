# !/usr/bin/python
# -*- coding: utf-8 -*-

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    assert type(x) is int
    assert type(b) is int and b >= 2
    p = 0
    while True:
        if x >= pow(b, p):
            max_p = p
            p += 1
        else:
            break
    return max_p
