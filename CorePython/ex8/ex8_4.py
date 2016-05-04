# !/usr/bin/env python
# -*- coding: utf-8 -*-


def isprime(num):
    x = num / 2
    while x > 1:
        if num % x == 0:
            is_prime = False
            break
        x -= 1
    else:
        is_prime = True
    return is_prime


def menu():
    num = int(raw_input("Enter the number: "))
    if isprime(num):
        print "It is a prime."
    else:
        print "It is NOT a prime."


if __name__ == '__main__':
    menu()
