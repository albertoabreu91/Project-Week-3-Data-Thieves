from requests_html import HTMLSession
from langdetect import detect
session = HTMLSession()
import pandas as pd
import requests
import re
import time
import random
# https://www.onlinenewspaperlist.com/
import urllib3

from bs4 import BeautifulSoup
with open('/home/josep/websites/Onlinenewsletter/www.onlinenewspaperlist.com/index.html', 'r') as html_page:
    html_page = html_page.read()

soup = BeautifulSoup(html_page, 'lxml')

data = soup.findAll('div', {'class': 'col_midle col_97'})
list_countys = []
list_countys_webs = []
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

    for div in data:
        links = div.findAll('a')
        for a in links:
            url = a.get('href')
            if url.startswith('htt') is True:
                contents = a.text
                x = x.replace("onlinenewspaperlist.com/",'' )
                x = x.replace(".html",'' )
                var = (url,x)
                list_countys_webs.append(var)
                print(x)
medias_list = list_countys_webs
print(list_countys_webs)
medias_list = set(list_countys_webs)

print(medias_list)

df = pd.DataFrame(medias_list)

df.to_csv('josep.csv', index=False)
josep_news_txt = open("josep_news_txt.txt", "a")     # Adding text at the end of the file

def get_language(website,country):

    print('here')
    print(website)
    url = website
    try:
        res = requests.get(url, verify=False, timeout=3)
        print(res)
        if res.status_code == 200:
            html_page = res.content
            soup = BeautifulSoup(html_page, 'html.parser')
            print(type(soup))
            text = list(soup)
            text =str(text)
            if text == None:
                return 'NaN'
            text = re.sub('<\s*?script[\s\S]*?(/script>)\W|<[^>]*>','', text)
            text.strip('\n').strip('\r')
            text.rstrip('\n').rstrip('\r ')
            text.lstrip('\n').lstrip('\r')
            val_lang = detect(text)
            josep_news_txt.write(website + "," + country + "," + val_lang + "\n")
            time.sleep(random.randint(0,8))
            return val_lang
        else:
            time.sleep(random.randint(0,8))
            return 'NaN'
    except:
        time.sleep(random.randint(0,8))
        return 'NaN'

df['lg'] = df.apply(lambda row: get_language(row[0],row[1]), axis=1)
print(df.head(50))
df.to_csv('josep2.csv', index=False)
