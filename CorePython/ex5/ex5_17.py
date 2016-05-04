# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def ran():
    list1 = []; list2 = []
    for N in range(0, random.randint(1, 100)):
        list1.append(random.randint(0, 2 ** 31 - 1))
    for M in range(0, random.randint(1, 100)):
        list2.append(random.choice(list1))
    return sorted(list2)
    