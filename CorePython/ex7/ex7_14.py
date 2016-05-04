# !/usr/bin/env python
# -*- coding: utf-8 -*-

from ex7_13 import creat_num, creat_set


def test1():
    a = creat_set()
    b = creat_set()
    print "set A is: %r.\nset B is: %r." % (a, b)
    aob = a | b
    anb = a & b
    print "A | B =\n(Please write the answer in a list.)"
    guess(aob)
    print "A & B =\n(Please write the answer in a list.)"
    guess(anb)


def guess(result):  # incorrect!
    for i in range(3):
        guess = raw_input("> ")
        if guess == result:
            print "Congratulations!"
            break
        else:
            print "Incorrect."
    print "The real one is %s." % result


if __name__ == '__main__':
    test1()
