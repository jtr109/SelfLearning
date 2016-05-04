# !/usr/bin/python
# -*- coding: utf-8 -*-

import re
from time import ctime


def check():
    try:
        data = open('redata.txt', 'r')
        lines = data.readlines()
        patt = '(.+?)::.+?(\d+)'
        same = True
        for line in lines:
            st = re.match(patt, line).group(1)
            t = re.match(patt, line).group(2)
            if st != ctime(int(t)):
                same = False
        return same
    finally:
        data.close()


if __name__ == '__main__':
    if check():
        print('Pass!')
    else:
        print('WTF!!!')
