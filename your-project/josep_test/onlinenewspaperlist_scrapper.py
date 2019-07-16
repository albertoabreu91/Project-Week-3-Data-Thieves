from requests_html import HTMLSession
session = HTMLSession()
import pandas as pd

# https://www.onlinenewspaperlist.com/
import urllib3
import requests
from bs4 import BeautifulSoup
with open('/home/josep/websites/Onlinenewsletter/www.onlinenewspaperlist.com/index.html', 'r') as html_page:
    html_page = html_page.read()

soup = BeautifulSoup(html_page, 'lxml')

data = soup.findAll('div', {'class': 'col_midle col_97'})
list_countys = []
for div in data:
    links = div.findAll('a')
    for a in links:
        url = a.get('href')
        contents = a.text
        if url.startswith('..') is True:
            url = url[3:]
            var = (url, contents)
            list_countys.append(var)

for x in list_countys:
    x = x[0]
    with open('/home/josep/websites/Onlinenewsletter/' + x, 'r') as html_page2:
        html_page2 = html_page2.read()
        html_page2 = str(html_page2)
        html_page2.encode('utf-8').decode("utf-8")

    soup = BeautifulSoup(html_page2, 'html.parser')

    data = soup.findAll('div', {'class': 'topsitelink_contain clr-fix'})
    list_countys_webs = []
    for div in data:
        links = div.findAll('a')
        for a in links:
            url = a.get('href')
            if url.startswith('htt') is True:
                contents = a.text
                var = (url,x)
                print(var)
print(list_countys_webs)
