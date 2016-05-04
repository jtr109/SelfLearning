# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
try:
    int('abc')
    print "bull shit try 1"
except ValueError:
    print "bull shit except 1"
else:
    print "bull shit else 1"


try:
    int(3.14)
    print "bull shit try 2"
except ValueError:
    print "bull shit except 2"
else:
    print "bull shit else 2"


try:
    try:
        int('abc')
        print "bull shit try 3"
    except ValueError:
        print "bull shit except 3"
    else:
        print "bull shit else 3"
finally:
    print "bull shit finally 3"
print "bull shit 3"
'''

def tr1():
    try:
        try:
            int('abc')
            print "bull shit try 4"
            return 1
        except ValueError:
            print "bull shit except 4"
    finally:
        print "bull shit finally 4"
    print "bull shit 4"


def tr2():
    try:
        try:
            int(123)
            print "bull shit try 4"
            return 1
        except ValueError:
            print "bull shit except 4"
    finally:
        print "bull shit finally 4"
    print "bull shit 4"


print tr1()
print '\n'
print tr2()
