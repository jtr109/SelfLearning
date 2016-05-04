# !/usr/bin/env python
# -*- coding: utf-8 -*-

def sort_key(dict1):
    sorted_keys = sorted(dict1)
    n = 0
    for k in sorted_keys:
        print "key%d: %r, value: %r" % (n, k, dict1[k])
        n += 1


def sort_value(dict2):
    sort_values = sorted(dict1.values())
    n = 0
    for v in sort_values:
        for k in dict1.keys():
            if v == dict1[k]:
                print "key%d: %r, value: %r" % (n, k, dict1[k])
                n += 1

'''
dict1 = dict(zip(('c', 'b', 'a', 'd'), ('gh', 'ab', 'ef', 'cd')))
sort_key(dict1)
print "\n"
sort_value(dict1)
'''
