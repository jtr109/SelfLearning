# !/usr/bin/env python
# -*- coding: utf-8 -*-


def search():
    key_byte = int(raw_input("Byte(0~255): "))
    obj_file = raw_input("File: ")
    f = open(obj_file, 'r')
    f_list = f.readlines()
    f_text = ''.join(f_list)
    key_char = chr(key_byte)
    cnt = f_text.count(key_char)
    print cnt


if __name__ == '__main__':
    search()
