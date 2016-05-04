# !/usr/bin/env python

import random


def create_file():
    obj_file = raw_input("File: ")
    key_byte = int(raw_input("Byte(0~255): "))
    cnt = int(raw_input("Times: "))
    text_len = int(raw_input("The length of text: "))
    byte_list = range(255)[:key_byte] + range(127)[key_byte+1:]
    text_list = []
    for n in range(text_len):
        text_list.append(random.choice(byte_list))
    i = 0
    key_list = []
    while i < cnt:
        key = random.randint(0, text_len-1)
        if key not in key_list:
            key_list.append(key)
            i += 1
    for k in key_list:
        text_list[k] = key_byte
    print text_list
    text_file = []
    for t in text_list:
        text_file.append(chr(t))
    text = ''.join(text_file)
    print text


if __name__ == '__main__':
    create_file()
