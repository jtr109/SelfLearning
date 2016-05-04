# !/usr/bin/env python
# -*- coding: utf-8 -*-

members = {}

def menu():
    prompt1 = '''Welcome to the HROA!
Please choose the mode:
1) add members;
2) show by name;
3) show by number;
'''
    while True:
        choice = raw_input(prompt1)
        # todo: complete it later
        if choice == '1':
            add()
        if choice == '2':
            name()
        if choice == '3':
            number()
        else:
            print "Please try again!"


def add():
    finish = False
    while True:
        name = raw_input("the name is: ")
        number = int(raw_input("the number is: "))
        members[name] = number
        cont = raw_input("Continue? (Y/N) ").lower()
        if cont == 'n':
            break


def name():
    names = []
    for member in members:
        names.append(member)
    st_names = sorted(names)
    for name in st_names:
        print("%s\t%d\n") % (name, members[name])


def number():
    numbers = []
    from ex7_7 import up_side_down
    members2 = up_side_down(members)
    for member in members2:
        numbers.append(member)
    st_numbers = numbers
    for number in st_numbers:
        print("%s\t%d\n") % (members2[number], number)


if __name__ == '__main__':
    menu()
