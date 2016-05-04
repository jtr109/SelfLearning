# !/usr/bin/python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    print(name, ' & ' ,addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '357626927@qq.com'  # input('From: ')
password = input('Password: ')
to_addr = 'lyp920109@outlook.com'  # input('To: ')
smtp_server = 'smtp.qq.com'  # input('SMTP server: ')

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python fan <%s>' % from_addr)
msg['To'] = _format_addr('Administer <%s>' % to_addr)
msg['Subject'] = Header('Hello from SMTP...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
