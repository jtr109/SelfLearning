# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
# map（f(n),[]) map提取iterator中的每个元素，调用f(n)计算，得出惰性数列，用list列表化
print(L2)
