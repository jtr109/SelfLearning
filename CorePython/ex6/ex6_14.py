# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def rochambeau():
    all_choice = "RPS"
    your_choice = raw_input('''Please choice in "(R)ock", "(P)aper" or "(S)cissors".
Your choice is: ''').upper()
    computer_choice = random.choice(all_choice)

# haven't be finished
