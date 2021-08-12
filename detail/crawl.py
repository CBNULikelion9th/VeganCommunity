import requests as r
import urllib.request as ur
import os
from dotenv import load_dotenv

def crawling(item):
    load_dotenv(verbose=False)
    GOOGLE_SEARCH_ENGINE_KEY = os.getenv('GOOGLE_SEARCH_ENGINE_KEY')

    engineid = "e885abd5f563ddafb"

    url = "https://www.googleapis.com/customsearch/v1"

    param = {
        "key":GOOGLE_SEARCH_ENGINE_KEY,

        "cx":engineid,

        "fileType":"jpg",

        "imgType" : "face",

        "q" : item,

        "searchType" : "image",

        "num" : 10,

        "start" : 1

        }

    s = r.Session()

    test = s.get(url,params=param).json()

    imglink = test.get('items')[1].get('link')

    return imglink
