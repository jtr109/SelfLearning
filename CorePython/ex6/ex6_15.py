# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def days_in_string(date):
    date_list = date.split('/')
    for i in range(len(date_list)):
        date_list[i] = int(date_list[i])
    return days_in_number(date_list)


def days_in_number(date_list):
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    tot = days_before_newyear(year) + days_in_year(month, day, year)
    return tot


def days_before_newyear(year):
    tot = 0
    for y in range(0, year):
        if leap_year(y):
            tot += 366
        else:
            tot += 365
    return tot


def days_in_year(month, day, year):
    tot = 0
    leap = leap_year(year)
    for m in range(1, month):
        if m in [1, 3, 5, 7, 8, 10]:
            tot += 31
        elif m in [4, 6, 9, 11]:
            tot += 30
        elif leap:
            tot += 29
        else:
            tot += 28
    tot += day
    return tot


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def days_between_two_days():
    print "Please input the two date. (the type is:MM/DD/YYYY)"
    date1 = raw_input("one date is:\n> ")
    date2 = raw_input("another date is:\n> ")
    dist = abs(days_in_string(date1) - days_in_string(date2))
    if dist == 0:
        print "These two date are same."
    elif dist == 1:
        print "There is 1 day between these two days."
    else:
        print "There are %d days between these two days.\n" % dist


def last_birthday():
    date1 = raw_input("Please input your birthday (the type is:MM/DD/YYYY).\n> ")
    today = datetime.date.today()
    date2 = [today.month, today.day, today.year]
    dist = abs(days_in_string(date1) - days_in_number(date2))
    print "You have live for %d days.\n" % dist


def next_birthday():
    date1 = raw_input("Please input your birthday (the type is:MM/DD/YYYY).\n> ")
    today = datetime.date.today()
    date2 = [today.month, today.day, today.year]
    birthday_coming = date1[:-4] + str(today.year)
    dist = days_in_string(birthday_coming) - days_in_number(date2)
    if dist < 0:
        birthday_coming = date1[:-4] + str(today.year + 1)
        dist = days_in_string(birthday_coming) - days_in_number(date2)
    print "Your next birthday is in %s.\nIt is %s day(s) later.\n" % (birthday_coming, dist)


def days_counter():
    while True:
        print ('Please choose the mode:\n'
               '1: Days Between Two Dates.\n'
               '2: Last Birthday.\n'
               '3: Next Birthday.')
        choice = raw_input('> ')
        if choice == '1':
            days_between_two_days()
        elif choice == '2':
            last_birthday()
        elif choice == '3':
            next_birthday()
        else:
            break

if __name__ == '__main__':
    days_counter()