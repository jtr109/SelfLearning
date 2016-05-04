# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
from time import ctime
from re import match

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
patt = '\((.+?)\)(.+)'

try:
    print 'Welcome to the chat room!'
    while True:
        dt, addr = udpSerSock.recvfrom(BUFSIZ)
        m = match(patt, dt)
        print m.group(1), '(' + ctime() + '):\n' + m.group(2)
        # udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
finally:
    udpSerSock.close()
