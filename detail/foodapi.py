from urllib.request import Request, urlopen
import json
import urllib
import urllib.request as ur
import os

def read_data():
    GOOGLE_SEARCH_ENGINE_KEY = os.environ.get('GOOGLE_SEARCH_ENGINE_KEY2')

    startRow = 1
    endRow = 150
    url = 'http://openapi.foodsafetykorea.go.kr/api/'+GOOGLE_SEARCH_ENGINE_KEY+'/I2790/json/'+str(startRow)+'/'+str(endRow)
    
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode('utf-8'))

    foodset = result['I2790']['row']
    # index = []
    # food_list= []
    # for i in range(0,len(result["I2790"]["row"])):
    #     food_list.append(foodset[i]["DESC_KOR"])

    #     index.append(i)
    # context = {
    #     'food_list':food_list,
    #     'index':index
    # }
    return foodset
