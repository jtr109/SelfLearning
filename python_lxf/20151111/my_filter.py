# !/usr/bin/python
# -*- coding: utf-8 -*-

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

if __name__ == '__main__':
    output = filter(is_palindrome, range(1, 1000))
    print(list(output))
