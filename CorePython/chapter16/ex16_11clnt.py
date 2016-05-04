# !/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

PORT = 80
BUFSIZ = 1024
host = 'www.apple.com'

# host = None
# while not host:
#     name = raw_input('Name: ')

ADDR = (host, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

tcpCliSock.send('GEThttp://class/download.microtool.de:80/somedata.exe\nHost:download.microtool.de\nAccept:*/*\nPragma:no-cache\nCache-Control:no-cache\nReferer:http://class/download.microtool.de/\nUser-Agent:Mozilla/4.04[en](Win95;I;Nav)\nRange:bytes=554554-')
data = tcpCliSock.recv(BUFSIZ)
print data

tcpCliSock.close()
