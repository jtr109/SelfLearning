# !/usr/bin/env python3
# -*- coding: utf-8 -*-

h = input('请输入您的身高（米）：')
w = input('请输入您的体重（千克）：')
height = float(h)
weight = float(w)

bmi = weight / (height ** 2)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
