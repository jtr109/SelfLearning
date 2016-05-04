# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

"""
hst = raw_input('Host: ')
pt = raw_input('Port: ')
if hst and pt:
    HOST = hst
    PORT = pt
"""

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
try:
    while True:
        print "It's your turn!"
        while True:
            data = raw_input("> ")
            # data += ' '
            if data == '':
                tcpCliSock.send('')
                break
            else:
                tcpCliSock.send(data)

        print "Waiting for clnt..."
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if data == '':
                break
            else:
                print data

finally:
    tcpCliSock.close()

# todo: should be debug
