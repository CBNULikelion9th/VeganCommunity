from urllib.request import urlopen
from bs4 import BeautifulSoup

url_list = [
    "https://smartstore.naver.com/soommask/products/4828127993",
    "https://smartstore.naver.com/aseado/products/4837257765",
    "https://smartstore.naver.com/aseado/products/4837266971",
    "https://smartstore.naver.com/aseado/products/3765693172",
    "https://smartstore.naver.com/aer-shop/products/4722827602",
    "https://smartstore.naver.com/aer-shop/products/4722827602",
    "https://smartstore.naver.com/korea-mask/products/4825762296",
    "https://m.smartstore.naver.com/ygfac/products/3905641271",
    "https://smartstore.naver.com/gonggami/products/4705579501"
];

def getClassValue(url, tag, className):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.body.find(tag,{"class", className})
    return content.text  

def getNameValue(url, tag, name) :
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.find(tag, {"name": name})
    return content.get('value')  

def getshop():
    # from .jsondata.cate4_data import url_list, getClassValue, getNameValue

    titles = []
    tag = 'a'
    className = 'basicList_link__1MaTN'
    for url in url_list :
        titles.append(getClassValue(url, tag, className))
    print(titles)

    prices = []
    tag = 'span'
    # className = 'basicList_price__2r23_'
    className = "price_num__2WUXn"
    for url in url_list :
        prices.append(getNameValue(url, tag, className))
    print(prices)

    filter_list2 = {
        'titles':titles,
        'prices':prices
    }

    return filter_list2