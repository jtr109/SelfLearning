#!/usr/bin/python
# -*- coding: utf-8 -*-

def mergeSort(numbers):
    numberOfElement = len(numbers)
    if numberOfElement < 2:
        return numbers
    else:
        mid = numberOfElement / 2
        L = numbers[:mid]
        R = numbers[mid:]

        L = mergeSort(L)
        R = mergeSort(R)

        newNumbers = []

        while L and R:
            if L[0] < R[0]:
                newNumbers.append(L[0])
                L.pop(0)
            else:
                newNumbers.append(R[0])
                R.pop(0)

        if L:
            newNumbers += L
        else:
            newNumbers += R

        return newNumbers


if __name__ == '__main__':
    numbers = [4, 2, 6, 8, 1, 3, 7, 5]
    newNumbers = mergeSort(numbers)
    print newNumbers
