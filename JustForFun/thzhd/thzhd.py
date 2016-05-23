#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urlparse

MAX = 100
FILENAME = 'new'
path = 'http://thzhd.info/forum-182-1.html' # OuMei


def getWholePage(path):
    res = requests.get(path)
    html_of_page = BeautifulSoup(res.text, "html.parser")
    print '** "%s" has been loaded.' % path
    return html_of_page


def getTorrent(path):
    html_of_page = getWholePage(path)
    a = html_of_page.select("div.f_c a")
    href = a[1].get('href')
    return href


def getFromPage(path, f):
    html_of_page = getWholePage(path)
    h2 = ''

    title = html_of_page.select("span#thread_subject")[0].string.encode('utf-8')
    h2 += '<h2>' + title + '</h2>\n'
    f.write(h2)

    for img in html_of_page.select('img.zoom'):
        src = img.get('file')
        f.write('<p><img src="' + src + '"></p>\n')

    link = html_of_page.select("p.attnm a")[0]
    string_of_link = link.string
    href_of_link = urlparse.urljoin(path, link.get('href'))
    href = getTorrent(href_of_link)
    # print string_of_link
    # print href_of_link
    a = '<p><a href="' + href + '" target= "_blank">' + string_of_link + '</a></p>\n'
    f.write(a)

    print '** "%s" had been writen.' % title


def getPageList(path, f):
    html = getWholePage(path)

    list_of_pages = html.select('a.s.xst')
    del list_of_pages[0]
    i = 0  #
    for link in list_of_pages:
        href_of_link = urlparse.urljoin(path, link.get('href'))
        getFromPage(href_of_link, f)
        i += 1  #
        if i > MAX:  #
            break  #


def getWholeHtml(path):
    html_name = FILENAME + '.html'
    f = open(html_name, 'w')
    head = '<!DOCTYPE HTML>\n' \
           '<html>\n' \
           '<head>\n' \
           '<link rel="stylesheet" type="text/css" href="mystyle.css">\n' \
           '</head>\n'\
           + '<body>\n'
    f.write(head)
    f.close()

    f = open(html_name, 'a')
    getPageList(path, f)
    f.write('</body>\n</html>\n')
    f.close()
    print "** ALL DONE! **"

if __name__ == '__main__':
    getWholeHtml(path)
