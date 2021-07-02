from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus
from urllib import parse
import urllib
import requests
import json

import urllib.request as ul
import xmltodict
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def info():
    url = 'http://apis.data.go.kr/1470000/FoodRwmatrInfoService/getFoodRwmatrList'
    key= 'A3ZJhyl76c9RGZ10B3pdDaxsqL%2F%2FLBGjaMAvwcnVMQ7i%2B4tL%2BomAYouEYEKXLfNmHWAANnGGg5VAS0fUrsk%2BHA%3D%3D'
    # queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'A3ZJhyl76c9RGZ10B3pdDaxsqL//LBGjaMAvwcnVMQ7i+4tL+omAYouEYEKXLfNmHWAANnGGg5VAS0fUrsk+HA==', quote_plus('rprsnt_rawmtrl_nm') : 'Abiu열매', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '3' })
    queryParams = f'?{parse.quote_plus("ServiceKey")}={key}&' + parse.urlencode({ quote_plus('rprsnt_rawmtrl_nm') : 'Abiu열매', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '3' })

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    #make dict datas
    # getJson = json.loads(response_body)["response"]["body"]
    # retItems = {}
    # i=0
    # for item in getJson["items"]["item"] :
    #     item = dict( item.items() )
    #     retItems['item'+str(i)] = ( json.dumps(item,ensure_ascii=False) )
    #     i += 1
    # return retItems

    dictionary = xmltodict.parse(response_body)
    json_object = json.dumps(dictionary)
    dictionary = json.loads(json_object)
    # print(type(json_object))
    return dictionary
    # context = {'food_info':json_object}
    # return render(request,'detail/main.html',context)
    # print(json_object)
