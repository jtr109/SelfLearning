# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)


def login():
    try:
        username = raw_input('What is your name?\n> ')
        print 'Have fun,' + username + '.'
        while True:
            data = raw_input('> ')
            if data == '(exit)':
                print 'Bye!'
                break
            dt = '(' + username + ')' + data
            udpCliSock.sendto(dt, ADDR)
    finally:
        udpCliSock.close()

if __name__ == '__main__':
    login()
