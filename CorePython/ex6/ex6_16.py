# !/usr/bin/env python
# -*- coding: utf-8 -*-


def matrix_addition(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        m = len(a)
        n = len(b)
        c = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                c[i][j] = a[i][j] + b[i][j]
        return c
    else:
        return "Error1: "


def matrix_multiplication(a, b):
    if len(a[0]) == len(b):
        m = len(a)
        l = len(a[0])
        n = len(b[0])
        c = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                for t in range(l):
                    c[i][j] += a[i][t] + b[t][j]
        return c
    else:
        return "Error2: "
