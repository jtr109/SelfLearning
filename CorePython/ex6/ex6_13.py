# !/usr/bin/env python
# -*- coding: utf-8 -*-


def atoc(string):
    len_string = len(string)
    for i in range(len_string - 1, 0, -1):
        if string[i] == '+' or string[i] == '-':
            real = float(string[:i])
            imag = float(string[i:-1])
            break
    number = complex(real, imag)
    return number

'''
# test
print atoc('-1.23e+4-5.67j')
print atoc('-1.23e-4+5.67j')
print atoc('-1.234-5.67j')
'''
