# !/usr/bin/env python
# -*- coding: utf-8 -*-

def change(dollars):
    line1 = "%.2f dollars can be changed in:" % dollars
    cents = int(dollars * 100)
    cent = (25, 10, 5, 1)
    ret = ""
    for c in cent:
        n = cents // c
        if n != 0:
            ret = ret + "\n%d of %d cents" % (n, c)
            cents = cents % c
    
    return line1 + ret
    