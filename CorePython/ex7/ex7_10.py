# !/usr/bin/env python
# -*- coding: utf-8 -*-


def rot13(sentence):
    new_list = []
    for char in sentence:
        ord_char = ord(char)
        if 65 <= ord_char <= 77 or 97 <= ord_char <= 109:
            new_char = chr(ord_char + 13)
            new_list.append(new_char)
        elif 78 <= ord_char <= 90 or 110 <= ord_char <= 122:
            new_char = chr(ord_char - 13)
            new_list.append(new_char)
        else:
            new_list.append(char)
    new_sentence = ''.join(new_list)
    return new_sentence


def menu():
    sentence = raw_input("Enter string to rot13: ")
    print "Your string to en/decrypt was: [%s]." % sentence
    new_sentence = rot13(sentence)
    print "The rot13 string is: [%s]." % new_sentence


if __name__ == '__main__':
    menu()
