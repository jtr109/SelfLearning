# !/usr/bin/env python
# -*- coding: utf-8 -*-


def rule(name):
    n = name.split()
    count = 0
    if n[0][-1] != ',':
        print ">> Wrong format... should be Last, First."
        print ">> You have done this 1 time(s) already. Fixing input..."
        count += 1
        n[0] = ''.join([n[0], ','])
    return ' '.join([n[0], n[1]])


def menu():
    name_list = []
    number = int(raw_input("Enter total number of names: "))
    for n in range(number):
        print "Please enter name %d:" % n,
        name = raw_input()
        name_list.append(rule(name))
    print "\nThe sorted list (by last name) is:"
    sorted_name = sorted(name_list)
    for name in sorted_name:
        print name


if __name__ == '__main__':
    menu()
