from urllib.request import Request, urlopen
import json
import urllib
import os
from dotenv import load_dotenv

def read_data():
    load_dotenv(verbose=False)
    GOOGLE_SEARCH_ENGINE_KEY = os.getenv('GOOGLE_SEARCH_ENGINE_KEY2')
    startRow = 1
    endRow = 150
    url = 'http://openapi.foodsafetykorea.go.kr/api/'+str(GOOGLE_SEARCH_ENGINE_KEY)+'/I2790/json/'+str(startRow)+'/'+str(endRow)
    
    data = urllib.request.urlopen(url).read().decode('utf-8')
    output = json.loads(data)

    return output
