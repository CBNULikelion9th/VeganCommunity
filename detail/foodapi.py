from urllib.request import Request, urlopen
import json
import urllib
import urllib.request as ur
import os

def read_data():
    GOOGLE_SEARCH_ENGINE_KEY = os.environ.get('GOOGLE_SEARCH_ENGINE_KEY2')

    startRow = 151
    endRow = 200
    url = 'http://openapi.foodsafetykorea.go.kr/api/'+GOOGLE_SEARCH_ENGINE_KEY+'/I2790/json/'+str(startRow)+'/'+str(endRow)
    
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode('utf-8'))

    foodset = result['I2790']['row']
    # print(foodset)
    return foodset
