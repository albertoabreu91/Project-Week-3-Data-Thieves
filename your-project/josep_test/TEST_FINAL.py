'''
import urllib2
response = urllib2("http://virdish.com")
page_source = response.read()
print(page_source)
'''
import pprint
from bs4 import Comment
from requests_html import HTMLSession
session = HTMLSession()
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import time
import random
# sting_to_analyze = input("Wich event you want to analyze: ")


import pandas as pd
table = pd.read_csv('josep_news_txt.csv')

def save_articles(web,pais,language):
    start_num = 0
    try:
        while True:
            josep_news_articles = open("josep_news_articles.txt", "a")

            topic = "refugees"
            date_from_mmddyyyy = "07/09/2019"
            date_to_mmddyyyy = "07/15/2019"


            google_bf = "https://www.google.com/search?q=site:"


            date_from = "&tbs=cdr%3A1%2Ccd_min:"
            date_to = "%2Ccd_max:"
            num = '&num=100'
            start_str = '&start='

            start_num = str(start_num)
            filter = "&filter=0"

            website = web

            print(topic)
            blob = TextBlob(topic)
            topic = str(blob.translate(to=language))

            content = '+"' + topic + '"'
            # "date_from + date_from_mmddyyyy + date_to + date_to_mmddyyyy"
            url_to_search = google_bf + website + content + "&tbs=qdr:w" + num + start_str + start_num + filter
            print(url_to_search)
            '''
            proxies = {
                        "http": 'http://209.50.52.162:9050',
                        "https": 'http://209.50.52.162:9050'
                        }
            '''
            r = requests.get(url_to_search, verify=True)
            print(r.text)
            time.sleep(random.randint(0,8))
            if r.status_code == 200:
                print('HERE1')

                r = str(r.text)
                r.encode('utf-8').decode("utf-8")
                soup = BeautifulSoup(r, 'html.parser')

                print('HERE2')
                data = soup.findAll('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'})
                if soup.findAll('div', {'class': 'nMymef MUxGbd lyLwlc'}):   #check if there is button suguiente
                    for div in data:
                        print('HERE3')
                        data2 = div.find('div', {'class': 'jfp3ef'})
                        data3 = div.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
                        if data2:
                            for div2 in data2:
                                print('HERE4')
                                print(div2)
                                links = div.findAll('a')
                                for a in links:
                                    print('HER54')
                                    url = str(a.get('href'))
                                    num = url.find('&')
                                    url = url[7:num]
                                titles = div.findAll('div', {'class': 'ZINbbc xpd O9g5cc uUPGi'})
                                for a2 in links:
                                    print('HER64')
                                    title = str(a2.contents[0])
                                    print(title)
                                    title = title[34:-6]
                                    title = title.replace(',', '')
                        if data3:
                            for div4 in data3:
                                data4 = div4.findAll('div', {'class': 'BNeawe s3v9rd AP7Wnd'})

                                for div5 in data4:
                                        print('HER74')
                                        if div5.contents[0]:
                                            title2 = str(div5.contents[0])
                                            title2 = title2[28:-7]
                                            title2 = title2.replace(',', '')
                                            title2 = title2.replace('.', '')
                                            print(title2)
                                        if len(div5.contents) >= 2:
                                            title3 = str(div5.contents[2])
                                            title3 = title3.replace(',', '')
                                            print(title3)
                        if title and url and title2 and title3:
                            josep_news_articles.write( title +  "," + url + "," + title2 + "," + title3 + "\n")

                        #span class="r0bn4c rQMQod date
                        #span class="r0bn4c rQMQod mensaje
            else:
                    return
    except:
        return

table.apply(lambda row: save_articles(row[0],row[1],row[2]), axis=1)
