# !/usr/bin/python
# -*- coding: utf-8 -*-

import base64


def safe_base64_decode(s):
    format_s = s + (4 - (len(s) % 4)) * '='
    return base64.urlsafe_b64decode(format_s)

if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print('Pass')
