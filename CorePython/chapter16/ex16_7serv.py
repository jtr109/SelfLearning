# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
try:
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr

        while True:
            print "Waiting for clnt..."
            while True:
                data = tcpCliSock.recv(BUFSIZ)
                if data == '':
                    print data + '!'
                    break
                else:
                    print data

            print "It's your turn!"
            while True:
                data = raw_input("> ")
                if data == ' ':
                    tcpCliSock.send('')
                    break
                else:
                    tcpCliSock.send(data)

finally:
    tcpSerSock.close()

# todo: should be debug
