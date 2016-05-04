# !/usr/bin/env python
# -*- coding: utf-8 -*-

def leap_year(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        # return "%d is a leap year." % y
        ly = True
    else:
        # return "%d is not a leap year." % y
        ly = False
    return ly
        