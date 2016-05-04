# !/usr/bin/env python
# -*- coding: utf-8 -*-


def payment():
    balance = float(raw_input("Enter opening balance: "))
    paid = float(raw_input("Enter monthly payment: "))
    print "Pymt#\tPaid\tAmount Remaining Balance"
    print "-----\t-----\t----------"
    pymt = 0
    print "%d\t$%2.2f\t$%3.2f" % (pymt, 0, balance)
    while balance > paid:
        balance -= paid
        pymt += 1
        print "%d\t$%2.2f\t$%3.2f" % (pymt, paid, balance)
    pymt += 1
    print "%d\t$%2.2f\t$%3.2f" % (pymt, balance, 0)
