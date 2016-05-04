# !/usr/bin/env python
# -*- coding: utf-8 -*-


def leap_year(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        ly = True
    else:
        ly = False
    return ly


def main():
    print filter(leap_year, range(1992, 2015))
    print [x for x in range(1992, 2015) if leap_year(x)]


if __name__ == '__main__':
    main()
