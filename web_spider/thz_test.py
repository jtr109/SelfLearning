# !/usr/bin/env python

import urllib
import urllib2

url = "http://thzhd.cc/forum.php"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3)'
# values = {'username': 'lyp920109@163.com', 'password': 'greedisg00d'}
headers = {'User-Agent': user_agent}
# data = urllib.urlencode(values)
request = urllib2.Request(url, headers=headers)
try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
else:
    print response.read()
