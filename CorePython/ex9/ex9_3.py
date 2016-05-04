# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_sc(path):  # file screening
    the_dir, the_file= os.path.split(path)
    os.chdir(the_dir)
    fobj = open(the_file, 'r')
    line_number = 0
    for eachLine in fobj:
        line_number += 1
    fobj.close()
    print line_number

file_sc(r'C:\Programs\CorePython\ex9\ospathex.py')