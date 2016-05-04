import requests
from bs4 import BeautifulSoup

res = requests.get('http://jandan.net/ooxx/page-1967#comments')
html = BeautifulSoup(res.text)
for index, each in enumerate(html.select('p img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(requests.get(each.attrs['src'], stream=True).content)

