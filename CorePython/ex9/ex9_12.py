# !/usr/bin/env python
# -*- coding: utf-8 -*-
# todo: (c) & (d) in ex7-5 should be finished one day...

import time
import random
import string
import hashlib
import shelve

path = r'C:\Programs\CorePython\ex9\tmp\db9_12.txt'


def getsalt():
    chars = string.letters+string.digits
    return random.choice(chars)+random.choice(chars)


def hash_pwd(pwd, salt):
    hashed = hashlib.md5()  # 创建一个MD5加密对象
    new_pwd = ''.join([pwd, salt])  # 加盐
    hashed.update(new_pwd)  # 更新要加密的数据
    return hashed.hexdigest()  # 加密后的结果，用十六进制字符串表示。


def newuser():
    prompt = 'login desired: '
    db = shelve.open(path)
    while True:
        name = raw_input(prompt).lower()
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('password: ')
    salt = getsalt()
    hashed_pwd = hash_pwd(pwd, salt)
    now = time.time()
    db[name] = [hashed_pwd, now, salt]
    db.close()


def olduser():
    name = raw_input('login: ').lower()
    db = shelve.open(path)
    pwd = raw_input('password: ')
    hashed_pwd = hash_pwd(pwd, db[name][2])
    true_pwd = db[name][0]
    if true_pwd == hashed_pwd:
        print 'welcome back', name
        db[name] = [db[name][0], last_login(db[name][1]), db[name][2]]
    else:
        print 'login incorrect'
    db.close()


def last_login(last):
    now = time.time()
    if now - last < 60:
        print "You already logged in at:", time.ctime(last)
    return now


def admin():
    prompt = '''
----------ADMINISTRATE----------
(D)elete a user
(S)how all user's informations
(B)ack
Enter choice:'''

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'b'
            print '\nYou picked: [%s]' % choice
            if choice not in 'dsb':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'b':
            done = True
        db = shelve.open(path)
        if choice == 'd':
            print 10 * '-', "Delete A User", 10 * '-'
            del_usr(db)
        if choice == 's':
            print 10 * '-', "All User's Information", 10 * '-'
            show_inf(db)
        db.close()


def del_usr(db):
    show_inf(db)
    prompt1 = "the user you want to delete is: "
    prompt2 = "Are you sure? (Y/N)\n> "
    usr = raw_input(prompt1)
    if usr in db:
        sure = raw_input(prompt2).strip()[0].lower()
        if sure == 'y':
            del db[usr]
            print "%r was deleted." % usr
    else:
        print "This name is not in the user list."


def show_inf(db):
    sorted_name = sorted(db.keys())
    for name in sorted_name:
        inf = (name, db[name][0], time.ctime(db[name][1]))
        print "Name: %s, Keyword: %s, Last login: %s" % inf
    print "------------------------------------------------------"


def showmenu():
    prompt1 = """
----------MENU----------
(N)ew User Login
(E)xisting User Login
(Q)uit
(A)dministrate
Enter choice: """

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt1).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print 'You picked: [%s]' % choice
            if choice not in 'neqa':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q': done = True
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'a': admin()


if __name__ == '__main__':
    showmenu()
