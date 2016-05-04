# !/usr/bin/env python

import urllib2

request = urllib2.Request("http://thzhd.cc/forum.php")
response = urllib2.urlopen(request)
print response.read()
