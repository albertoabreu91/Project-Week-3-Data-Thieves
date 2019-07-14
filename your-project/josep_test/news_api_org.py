from newsapi import NewsApiClient
import pandas as pd
import pprint
newsapi = NewsApiClient(api_key='a084595d62604623935b559f057c593a')



all_articles = newsapi.get_everything(q='messi')

table = pd.DataFrame(all_articles)
pprint.pprint(all_articles,indent=2)
