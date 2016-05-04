# !/usr/bin/env python
# -*- coding: utf-8 -*-


def idcheck():

    import string
    import keyword

    alphas = string.letters + '_'
    nums = string.digits

    print 'Welcome to the Identifier Checker v1.0'
    print 'Testees most be at least 1 chars long.'
    while True:
        myInput = raw_input('Identifier to test? ')

        if myInput in keyword.kwlist:
            print "invalid: the keyword can't be used"

        elif len(myInput) >= 1:
            if myInput[0] not in alphas:
                print 'invalid: first symbol must be alphabetic'
            else:
                for otherChar in myInput[1:]:
                    if otherChar not in alphas + nums:
                        print 'invalid: remaining symbols must be alphanumeric'
                        break
                else:
                    print "okay as an indentifier"
