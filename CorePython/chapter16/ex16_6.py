# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567  # getservbyname('daytime')
print 'PORT is %d' % PORT
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    prt = getservbyname('daytime')
    info = getaddrinfo(HOST, prt)
    if not data:
        break
    print data
    if not info:
        break
    print info


"""
    NADDR = (HOST, sv)
    udpCliSock.sendto('abc', NADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data


udpCliSock.close()
"""