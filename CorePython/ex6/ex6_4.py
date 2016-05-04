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


def grade():
    grades = []
    tot = 0.0
    while True:
        g = int(raw_input("> "))
        if 0 <= g <= 100:
            grades.append(level(g))
            tot += g
        else:
            print grades
            ave = tot / len(grades)
            print "The average is %.2f" % ave
            break
