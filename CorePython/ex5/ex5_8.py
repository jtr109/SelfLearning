# !/usr/bin/env python
# -*- coding: utf-8 -*-

def Squ(edge):
    area = edge ** 2
    volume = edge ** 3
    ret = "the area is %.2f\nthe volum is %.2f" % (area, volume)
    return ret
    
def Cir(radius):
    PI = 3.14159
    area = PI * (radius ** 2)
    volume = 4.0 / 3 * (radius ** 3)
    ret = "the area is %.2f\nthe volum is %.2f" % (area, volume)
    return ret