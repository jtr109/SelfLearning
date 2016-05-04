# !/usr/bin/python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = '357626927@qq.com'  # input('From: ')
password = 'lyp920109'  # input('Password: ')
# 输入收件人地址:
to_addr = 'lyp920109@163.com'  # input('To: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'  # input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()