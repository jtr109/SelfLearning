# !/usr/bin/python
# -*- coding: utf-8 -*-

def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L


if __name__ == '__main__':
    L = [3, 5, 2, 1, 4]
    modSwapSort(L)
