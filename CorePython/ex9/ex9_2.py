# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_sc(n, f):  # file screening
    the_dir, the_file = os.path.split(f)
    os.chdir(the_dir)
    fobj = open(the_file, 'r')
    line_number = 0
    for eachLine in fobj:
        if line_number < n:
            print eachLine,
        else:
            break
        line_number += 1
    fobj.close()


file_sc(7, r'C:\Programs\CorePython\ex9\ospathex.py')