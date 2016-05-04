# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(text1, text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            return