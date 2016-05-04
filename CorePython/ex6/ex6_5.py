# !/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


def pal(words):
    chr_list = list(words)
    rev_chr_list = copy.deepcopy(chr_list)
    rev_chr_list.reverse()
    if chr_list == rev_chr_list:
        print "palindrome!"
    else:
        new_list = chr_list + rev_chr_list
        new_words = ''.join(new_list)
        print '%s is not a palindrome.\n What about "%s"?' % (words, new_words)
