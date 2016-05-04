# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def spt():
    start_time = time.time()
    print "start_time is:", start_time
    n = 0
    for i in range(1, 10000000):
        n += i
    finish_time = time.time()
    print "finish time is:", finish_time
    sp_time = finish_time - start_time
    print "sp_time is:", sp_time
