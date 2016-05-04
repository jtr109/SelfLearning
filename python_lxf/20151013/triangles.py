#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
def triangles():
    L= [1]
    yield L
    while True:
        L.append(1)
        yield L
        L = [L[i] + L[i - 1] for i in range(len(L))]
        L.insert(0, 1)


n = 0
for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break

# False
'''

'''
def triangles(n):
    L = [1]
    while len(L) < n + 1:
        yield(L)
        L.append(0)
        L = [L[i] + L[i - 1] for i in range(len(L))]

for i in triangles(10):
    print(i)
'''


def triangles(m):
    L = [1]
    while len(L) <= m:
        '''m为要求行数（对应L的长度）'''
        yield(L)
        # 前置用于返回第一组L，循环中在generator里打印出新的一行L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
        # 生成新一组list
# triangle()中已生成整个杨辉三角形

for i in triangles(10):
    print(i)





































