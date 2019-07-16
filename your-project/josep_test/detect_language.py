'''
import requests
from bs4 import BeautifulSoup

url = 'http://www.alsahwa-yemen.net/'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head',
	'input',
	'script',
    'style',
    'footer-nav',
    'div',
    'a',
    'nav',
    'em',
    'p'
    '!--'
	# there may be more elements you don't want, such as "style", etc.
]

for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)

print(output)

from textblob import TextBlob
from lang_country import *

sting_to_analyze = input("Wich event you want to analyze: ")
string_to_analyze = output
blob = TextBlob(string_to_analyze)
print(blob.translate(to="ca"))
'''

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.morfix.co.il/website'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))
text = list(soup)
text =str(text[3])

text = re.sub('<\s*?script[\s\S]*?(/script>)\W|<[^>]*>','', text)
text.strip('\n').strip('\r')
text.rstrip('\n').rstrip('\r')
text.lstrip('\n').lstrip('\r')
print(text)

from langdetect import detect
print(detect(text))

from textblob import TextBlob

blob = TextBlob(text)
print(blob.translate(to="ca"))
