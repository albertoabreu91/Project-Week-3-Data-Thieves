
"""
 site:www.lavanguardia.com "refugiados"
https://www.google.com/search?q=site%3Awww.lavanguardia.com+%22refugiados%22&tbs=cdr%3A1%2Ccd_min%3A7%2F1%2F2019%2Ccd_max%3A7%2F13%2F2019&tbm=



from googlesearch import search


query = 'site:lavanguardia.com "refugiados" '

for j in search(query, num=10, start=0, stop=None, pause=3.5):
    print(j)

import webbrowser
# webbrowser.get('/usr/bin/google-chrome %s').open('http://virdish.com')
import urllib2
response = urllib2("http://virdish.com")
page_source = response.read()
print(page_source)

import pprint
from bs4 import Comment
from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.google.com/search?q=site%3Awww.lavanguardia.com+%22barça%22&tbs=cdr%3A1%2Ccd_min%3A7%2F1%2F2019%2Ccd_max%3A7%2F13%2F2019&tbm=')
print(r)
pprint.pprint(r.html.absolute_links)
pprint.pprint(r.raw)

"""
import pprint
from requests_html import HTMLSession
session = HTMLSession()
import pandas as pd


website_list_newspapers = "https://en.wikipedia.org/wiki/Lists_of_newspapers"
wiki_search = session.get(website_list_newspapers)
Wiki_result = pd.DataFrame(wiki_search.html.absolute_links)
Wiki_result = Wiki_result[Wiki_result[0].str.startswith("https://en.wikipedia.org/wiki/List_of_newspapers_in_")]
print(Wiki_result)
Wiki_result.to_csv('list_of_newspapers.csv')
