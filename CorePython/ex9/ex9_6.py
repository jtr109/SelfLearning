# !/usr/bin/env python
# -*- coding: utf-8 -*-


def comp(path1, path2):
    file1 = open(path1)
    file2 = open(path2)
    line = 0
    finish = False

    while not finish:
        line += 1
        line1 = file1.readline()
        line2 = file2.readline()
        if line1 != line2:
            len_max = max(len(line1), len(line2))
            for n in range(len_max):
                if line1[n] != line2[n]:
                    print "Different in Line %d, Number %d" % (line, n+1)
                    finish = True
                    break
        elif line1 == '':
                print "These 2 files are same!"
                finish = True

    file1.close()
    file2.close()


path1 = r'C:\Programs\CorePython\ex9\ex9_1.py'
path2 = r'C:\Programs\CorePython\ex9\ex9_2.py'
comp(path1, path2)
path3 = r'C:\Programs\CorePython\ex9\tmp\a.txt'
path4 = r'C:\Programs\CorePython\ex9\tmp\b.txt'
comp(path3, path4)
