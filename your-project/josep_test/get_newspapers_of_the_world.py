from requests_html import HTMLSession
session = HTMLSession()
import pandas as pd

# https://www.onlinenewspaperlist.com/
import urllib3
import requests
from bs4 import BeautifulSoup
import re


url = 'https://onlinenewspaperlist.com'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

# url = "http://www.gsmarena.com/samsung-phones-f-9-0-p2.php"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'lxml')
print(soup)
data = soup.findAll('div')
for div in data:
    links = div.findAll('a')
    for a in links:
        print("http://www.gsmarena.com/" + a['href'])

for tag in soup.findAll('a'):
    print (tag)
