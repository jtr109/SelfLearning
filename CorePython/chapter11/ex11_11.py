# !/usr/bin/env python
# -*- coding: utf-8 -*-


def map_strip(lines):
    new_lines = map(lambda t: t.strip(' '), lines)
    return new_lines


def list_strip(lines):
    new_lines = [t.strip(' ') for t in lines]
    return new_lines


def main():
    path = raw_input('File: ')
    f = open(path, 'r')
    lines = f.readlines()
    f.close()

    # new_lines = map_strip(lines)
    new_lines = list_strip(lines)

    prompt1 = "Mode: (Copy / Cover)\n> "
    while True:
        mode = raw_input(prompt1).lower()
        if mode == 'copy':
            new_path = raw_input("New path: ")
            nf = open(new_path, 'w')
            nf.writelines(new_lines)
            nf.close()
            break
        elif mode == 'cover':
            nf = open(path, 'w')
            nf.writelines(new_lines)
            nf.close()
            break
        else:
            print 'Try again!'


if __name__ == '__main__':
    main()
