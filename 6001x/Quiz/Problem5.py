# !/usr/bin/python
# -*- coding: utf-8 -*-

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Your Code Here
    lace_string = ''
    max_len = max(len(s1), len(s2))
    for i in range(max_len):
        lace_string += s1[i:i+1] + s2[i:i+1]
    return lace_string
