# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
from time import sleep

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        try:
            t = int(data)
            tcpCliSock.send('Server will sleep for %d second(s).' % t)
            sleep(t)
        except ValueError:
            tcpCliSock.send('Invalid time. Please send a number.')
            sleep(1)
        finally:
            tcpCliSock.send('Then?')


tcpSerSock.close()
