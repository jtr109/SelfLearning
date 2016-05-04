# !/usr/bin/env python
# -*- coding: utf-8 -*-


def adv_open(path, mode = 'r'):
    try:
        return open(path, mode)
    except:
        print "Adv open failed..."
        return None


f = adv_open(r"C:\Programs\CorePython\ex10\tmp\a.txt", 'w')
f.write('abc\n')
f.close()
