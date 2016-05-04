# !/usr/bin/python
# -*- coding: utf-8 -*-


def log(func):
    def wrapper(*args, **kw):
        print("begin call: %s" % func.__name__)
        ret = func(*args, **kw)
        print("end call: %s" % func.__name__)
        return ret
    return wrapper

if __name__ == '__main__':
    @log
    def now():
        print('2015-11-12')

    now()
