# !/usr/bin/python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = '357626927@qq.com'  # input('From: ')
password = input('Password: ')
to_addr = 'lyp920109@163.com'  # input('To: ')
smtp_server = 'smtp.qq.com'  # input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
