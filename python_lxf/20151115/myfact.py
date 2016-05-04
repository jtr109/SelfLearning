# !/usr/bin/python
# -*- coding: utf-8 -*-

def fact(n):
    '''
    >>> f3 = fact(3)
    >>> f3
    6
    >>> fact(2)
    2
    >>> fact(1)
    1
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(5)
    120
    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()