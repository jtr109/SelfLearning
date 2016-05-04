# !/usr/bin/env python
# -*- coding: utf-8 -*-

def Gcd(m, n):
    small_list = range(0, min(m, n) + 1)[::-1]
    for g in small_list:
        if m % g == 0 and n % g == 0:
            return g
    
def Lcm(m, n):
    return m * n / Gcd(m, n)