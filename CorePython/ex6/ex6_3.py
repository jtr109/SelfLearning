# !/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_item():
    item = raw_input('Please input the number:\n> ')
    item_list = list(item)
    sorted_list = sorted(item_list)
    new_item = ''.join(sorted_list)
    print "%s" % new_item
