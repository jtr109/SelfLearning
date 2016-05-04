# !/usr/bin/env python
# -*- coding: utf-8 -*-


def tr(srcstr, dststr, string):
    len_srcstr = len(srcstr)
    lower_srcstr = srcstr.lower()
    lower_string = string.lower()
    new_string = lower_string
    while True:
        n = new_string.find(lower_srcstr)
        if n == -1:
            break
        else:
            new_string = ''.join([string[:n], dststr, string[(n + len_srcstr):]])
    return new_string


def menu():
    while True:
        srcstr = raw_input('srcstr: ')
        dststr = raw_input('dststr: ')
        string = raw_input('string: ')
        new_string = tr(srcstr, dststr, string)
        print "The new string is: ", new_string


if __name__ == '__main__':
    menu()
