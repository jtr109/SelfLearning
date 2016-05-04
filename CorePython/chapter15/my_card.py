# !/usr/bin/python
# -*- coding: utf-8 -*-

import re


def is_legal(data):
    patt = '(\d{15,16})|(\d{4}-\d{6}-\d{5})|(\d{4}(-\d{4}){3})'
    try:
        for i in range(1, 4):
            if re.match(patt, data).group(i):
                pd = purify(data, i)
                return legal_card(pd)
    except AttributeError:
        return False


def purify(data, i):
    pn = ''
    if i == 1:
        pn = data
    else:
        l = data.split('-')
        for n in l:
            pn += n
    pd = []
    for a in pn:
        for b in a:
            pd.append(b)
    return pd


def legal_card(pd):
    pd.reverse()
    ns = 0
    w = 1
    for d in pd:
        if w % 2 == 1:
            d = int(d)
        else:
            d = 2 * int(d)
            if d > 9:
                d -= 9
        ns += d
        w += 1
    return ns % 10 == 0


if __name__ == '__main__':
    card_number = raw_input('Your card number is:\n> ')
    if is_legal(card_number):
        print 'It is a legal number!'
    else:
        print 'Shit! It is an illegal number!!!'
