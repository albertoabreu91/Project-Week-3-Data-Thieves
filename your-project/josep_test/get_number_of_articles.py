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
# sting_to_analyze = input("Wich event you want to analyze: ")

josep_news_articles = open("josep_news_articles.txt", "a")

topic = "refugees"
date_from_mmddyyyy = "07/09/2019"
date_to_mmddyyyy = "07/17/2019"


google_bf = "https://www.google.com/search?q=site:"


date_from = "&tbs=cdr%3A1%2Ccd_min:"
date_to = "%2Ccd_max:"
num = '&num=100'
start = '&start=0'
filter = "&filter=0"

test = ['https://www.lavanguardia.es','','es']
website = test[0]
lang = test[2]
sting_to_analyze = input("Wich event you want to analyze: ")
string_to_analyze = topic
blob = TextBlob(string_to_analyze)
topic = str(blob.translate(to=lang))
content = '+"' + topic + '"'


url_to_search = google_bf + website + content + date_from + date_from_mmddyyyy + date_to + date_to_mmddyyyy + num + start + filter
print(url_to_search)

r = requests.get(url_to_search)
print(r.text)
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
    print('NaN')

