# !/usr/bin/env python
# -*- coding: utf-8 -*-

def even():
    even_number = []
    for n in range(0, 21):
        if n % 2 == 0:
            even_number.append(n)
    return even_number

    
def odd():
    odd_number = []
    for n in range(0, 21):
        if n % 2 != 0:
            odd_number.append(n)
    return odd_number
    

def test(m, n):
    return not(bool(m % n))