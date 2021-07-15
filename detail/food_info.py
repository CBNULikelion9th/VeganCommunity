from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus
from urllib import parse
import urllib
import requests
import json

import urllib.request as ul
import xmltodict

def info():
    url = 'http://apis.data.go.kr/1470000/FoodRwmatrInfoService/getFoodRwmatrList'
    key= 'A3ZJhyl76c9RGZ10B3pdDaxsqL%2F%2FLBGjaMAvwcnVMQ7i%2B4tL%2BomAYouEYEKXLfNmHWAANnGGg5VAS0fUrsk%2BHA%3D%3D'
    queryParams = f'?{parse.quote_plus("ServiceKey")}={key}&' + parse.urlencode({ quote_plus('rprsnt_rawmtrl_nm') : 'Abiu열매', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '3' })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    dictionary = xmltodict.parse(response_body)
    json_object = json.dumps(dictionary)
    dictionary = json.loads(json_object)
    print(type(json_object))
    return dictionary

# info()