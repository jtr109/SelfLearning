# !/usr/bin/python
# -*- coding: utf-8 -*-

import os

result = []


def exi(chosen_dir, keyword):
    if os.path.isdir(chosen_dir):
        fd(chosen_dir, keyword)
    else:
        print("There is not such a directory.")


def fd(chosen_dir, keyword):
    for x in os.listdir(chosen_dir):
        x_path = os.path.join(chosen_dir, x)
        if os.path.isfile(x_path) and keyword in x:
            result.append(x_path)
        elif os.path.isdir(x_path):
            fd(x_path, keyword)


def fd_file():
    cwd = os.path.abspath('.')
    fd_dir = input("The absolute path of the directory:\n"
                   "(Current directory is '%s')\n> " % cwd)
    keyword = input("The keyword of a file:\n> ")
    exi(fd_dir, keyword)
    ab = len(fd_dir)
    for p in result:
        print(p[ab:])


if __name__ == '__main__':
    fd_file()
