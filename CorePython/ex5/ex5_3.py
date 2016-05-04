# !/usr/bin/env python
# -*- coding: utf-8 -*-


def level(num):
    if 0 <= num <= 100:
        if num >= 90:
            return "A"
        elif num >= 80:
            return "B"
        elif num >= 70:
            return "C"
        elif num >= 60:
            return "D"
        else:
            return "F"
    else:
        return "ERROR"
        