# !/usr/bin/env python
# -*- coding: utf-8 -*-


def stan(f, t):
    print "DEC\tBIN\tOCT\tHEX",
    if 33 <= t <= 126:
        print "ASCII",
    print "\n------------------------------------"
    if 33 <= t <= 126:
        for n in range(f, t+1):
            print "%d\t%s\t%s\t%s\t%s" % (n, mybin(n), myoct(n), myhex(n), chr(n))
    else:
        for n in range(f, t+1):
            print "%d\t%s\t%s\t%s" % (n, mybin(n), myoct(n), myhex(n))


def mybin(n):
    return int(bin(n)[2:])


def myoct(n):
    return oct(n)[1:]


def myhex(n):
    return hex(n)[2:]


def ex(n):
    count = 1
    while n > 1:
        n /= 2
        count += 1
    return count


def menu():
    f = int(raw_input("from: "))
    t = int(raw_input("to: "))
    stan(f, t)


if __name__ == '__main__':
    menu()

