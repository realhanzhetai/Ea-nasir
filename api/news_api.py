from dotenv import load_dotenv
import os
from newsapi import NewsApiClient

load_dotenv()
financial_news_token = os.getenv('newsapi')

newsapi = NewsApiClient(api_key=financial_news_token)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(sources='bloomberg',
                                          language='en')

print(top_headlines)


