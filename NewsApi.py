import os
import requests
from dotenv import load_dotenv
from random import choice
load_dotenv()

def get_top_headlines():
    
    url=f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv("NEWS_API_KEY")}"
    try:
        news=requests.get(url).json()
        articles= news['articles'][:5]
        # headlines=[a['title'] for a in articles]
        a=choice(articles)
        return a['title']
    except :
        return "Sorry, I couldn't get a news right now."
      