# !/usr/bin/python
# -*- coding: utf-8 -*-

def classtree*(cls, indent):
    print('.'* indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent+3)
        
def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)
    
def selftest():
    class A: pass
    class B(A): pass
    class C(A):
    
