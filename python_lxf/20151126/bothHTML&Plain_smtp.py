# !/usr/bin/python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '357626927@qq.com'  # input('From: ')
password = input('Password: ')
to_addr = 'lyp920109@outlook.com'  # input('To: ')
smtp_server = 'smtp.qq.com'  # input('SMTP server: ')

msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python fan <%s>' % from_addr)
msg['To'] = _format_addr('Administer <%s>' % to_addr)
msg['Subject'] = Header('Hello from SMTP...', 'utf-8').encode()
msg.attach(MIMEText('oops!', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

with open('/home/jtr109/mystuff/python_lxf/20151123/test.jpeg', 'rb') as f:
    mime = MIMEBase('inmage', 'jpeg', filename='test.jpeg')
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpeg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
