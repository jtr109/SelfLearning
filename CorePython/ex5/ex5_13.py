# !/usr/bin/env python
# -*- coding: utf-8 -*-

def time_exc(H_M):
    h_m = H_M.split(":")
    m = 60 * int(h_m[0]) + int(h_m[1])
    return m
    