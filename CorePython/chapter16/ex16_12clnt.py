# !/usr/bin/python
# -*- coding: utf-8 -*-
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    while data != 'Then?':
        data = tcpCliSock.recv(BUFSIZ)
        print data

tcpCliSock.close()
