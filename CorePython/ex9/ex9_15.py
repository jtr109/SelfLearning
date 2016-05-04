# !/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


def file_copy():
    prompt1 = "Copy from the file: "
    prompt2 = "Copy to the file: "

    cf = open(raw_input(prompt1), 'r')
    tmp_list = []
    for eachLine in cf:
        tmp_list.append(eachLine)
    tmp = ''.join(tmp_list)
    cf.close()

    ct = open(raw_input(prompt2), 'w')
    ct.write(tmp)
    ct.close()


if __name__ == '__main__':
    file_copy()