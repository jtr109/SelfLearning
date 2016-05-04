# !/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve

data = r'C:\Programs\CorePython\ex9\tmp\finance.txt'


def menu():
    prompt1 = '''########## MENU ##########
AA: add account
SA: show account
IC: income
EX: expense
CF: cash flow
Q:  quit
----- Please choose your operation -----'''
    while True:
        print prompt1
        kind = raw_input('> ').lower()
        if kind == 'q':
            print "See you!"
            break
        elif kind in ('aa', 'sa', 'ic', 'ex', 'cf'):
            operation(kind)
        else:
            print "Please enter the right abbreviation. Try again!"


def operation(kind):
    if kind == 'aa':
        add_account()
    elif kind == 'sa':
        show_accounts()
    elif kind == 'ic':
        income()
    elif kind == 'ex':
        expense()
    elif kind == 'cf':
        cash_flow()
    else:
        print "ERROR!!!"


def show_accounts():
    fobj = shelve.open(data)
    for ac in fobj:
        if ac != 'last operation':
            print "%s(%s): %d" % (ac, fobj[ac][0], fobj[ac][1])
    fobj.close()


def add_account():
    print "********** ADD ACCOUNT **********"
    prompt1 = '''Choose the kind of the new account:
CA: cash
CC: credit card
DC: deposit card
FM: financial market
(BM: back to menu)'''
    fobj = shelve.open(data)
    unsaved = True
    while unsaved:
        print prompt1
        while True:
            kind = raw_input('> ').lower()
            if kind == 'bm':
                menu()
            if kind in ('ca', 'cc', 'dc', 'fm', 'bm'):
                break
            else:
                print "Please enter the right abbreviation. Try again!"
        while True:
            account = raw_input("Name of the new account: ")
            if account == 'last operation' or account in fobj:
                print "This account is exist. Please try another name."
            else:
                break
        while True:
            fund = raw_input("Fund in the new account: ")
            try:
                fund = int(fund)
                break
            except ValueError:
                print "Not a number. Please try again!"
        print "The account you want to add:\n%s(%s): %d" % (account, kind, fund)
        if raw_input('Do you want to save? (Press "C" to cancel.)').lower() != 'c':
            unsaved = False
    fobj[account] = [kind, fund]
    print "Saving...\n"
    fobj.close()


def income():
    show_accounts()

    fobj = shelve.open(data)

    while True:
        account = raw_input("Account: ")
        if account not in fobj:
            print "Not found! Try again!"
        else:
            money = raw_input("Income: ")
            try:
                money = int(money)
                if money >= 0:
                    val = fobj[account]  # the value of shelve is static
                    val[1] += money  # it can't be modified
                    fobj[account] = val  # a mid value should be used
                    print "Saving...\n%s(%s): %d" % (account, fobj[account][0], fobj[account][1])
                    break
                else:
                    print "Not an income above 0. Please try again."
            except ValueError:
                print "Not a number. Please try again!"

    fobj.close()


def expense():
    show_accounts()

    fobj = shelve.open(data)

    while True:
        account = raw_input("Account: ")
        if account not in fobj:
            print "Not found! Try again!"
        else:
            money = raw_input("Expense: ")
            try:
                money = int(money)
                if money >= 0:
                    val = fobj[account]  # the value of shelve is static
                    val[1] -= money  # it can't be modified
                    fobj[account] = val  # a mid value should be used
                    print "Saving...\n%s(%s): %d" % (account, fobj[account][0], fobj[account][1])
                    break
                else:
                    print "Not an expense above 0. Please try again."
            except ValueError:
                print "Not a number. Please try again!"

    fobj.close()


def cash_flow():
    show_accounts()

    fobj = shelve.open(data)

    while True:
        fa = raw_input("From account: ")
        if fa not in fobj:
            print "Not found! Try again!"
        else:
            ta = raw_input("To account: ")
            if ta == fa:
                print "Same account! Try again!"
            elif ta not in fobj:
                print "Not found! Try again!"
            else:
                cf = raw_input("The cash flow: ")
                try:
                    cf = int(cf)

                    val = fobj[fa]
                    val[1] -= cf
                    fobj[fa] = val

                    val = fobj[ta]
                    val[1] += cf
                    fobj[ta] = val
                    print "Saving...\n%d had been moved from %s to %s." % (cf, fa, ta)
                    print "%s(%s): %d\n%s(%s): %d" % (fa, fobj[fa][0], fobj[fa][1],
                                                      ta, fobj[ta][0], fobj[ta][1],)
                    break
                except ValueError:
                    print "Not a number. Please try again!"


if __name__ == '__main__':
    menu()
