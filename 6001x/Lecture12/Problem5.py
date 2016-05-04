# !/usr/bin/python
# -*- coding: utf-8 -*-


def genPrimes():
    primes = []
    x = 2
    while True:
        for p in primes:
            if x % p == 0:
                break
        else:
            yield x
        primes.append(x)
        x += 1
