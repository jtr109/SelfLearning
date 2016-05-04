# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def file_sc(path):  # file screening
    the_dir, the_file= os.path.split(path)
    os.chdir(the_dir)
    fobj = open(the_file, 'r')
    for eachLine in fobj:
        sharp = eachLine.find('#')
        if sharp == -1:
            print eachLine,
        else:
            new_line = eachLine[0: sharp]
            print new_line
    fobj.close()


file_sc(r'C:\Programs\CorePython\ex9\ospathex.py')