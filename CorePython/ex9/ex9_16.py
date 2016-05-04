# !/usr/bin/env python
# -*- coding: utf-8 -*-


def text_processing():
    text_file = open(r"C:\Programs\CorePython\ex9\tmp\a.txt")
    tmp = text_file.readlines()
    text_file.close()

    new_tmp = []

    for line in tmp:
        new_line = []
        while len(line) > 80:
            sp = line[:80].rfind(' ')
            new_line.append(''.join([line[:sp], '\n']))
            line = line[(sp+1):]
        else:
            new_line.append(line)
        new_tmp.append(''.join(new_line))
    new_text = open(r"C:\Programs\CorePython\ex9\tmp\b.txt", 'w')
    new_text.writelines(new_tmp)


if __name__ == '__main__':
    text_processing()
