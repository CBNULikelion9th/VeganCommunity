from urllib.request import urlopen
from bs4 import BeautifulSoup

titles = []
prices = []

url_list = [
    "https://search.shopping.naver.com/search/all?query=%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC&frm=NVSHATC&prevQuery=%EC%8B%9D%EB%A3%8C%ED%92%88",    # 마켓컬리
    "https://search.shopping.naver.com/search/all?query=%EC%BF%A0%ED%8C%A1%20%EB%B0%98%EC%B0%AC&frm=NVSHATC&prevQuery=%EC%BF%A0%ED%8C%A1",          # 쿠팡
    "https://search.shopping.naver.com/search/all?query=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93&frm=NVSHATC&prevQuery=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93%20%EB%B0%98%EC%B0%AC",  # 푸드슈퍼마켓
    "https://search.shopping.naver.com/search/all?query=G%EB%A7%88%EC%BC%93%20%EB%B0%98%EC%B0%AC&frm=NVSHATC&prevQuery=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93"      # G마켓
]

def getClassValue(url, tag, className):
    filter_list2 = []
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.find_all(tag,{"class", className})
    # print(content)
    for i in content:
        filter_list2.append(i['title'])
    # print(filter_list2)
    return filter_list2

def getNameValue(url, tag, className) :
    price_list = []
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.find_all(tag, {"class": className})
    # print(content.get_text())
    for i in content:
        price_list.append(i.get_text())
    # print(price_list)
    return price_list

def getshop():

    tag = 'a'
    className = 'basicList_link__1MaTN'
    for url in url_list :
        titles.append(getClassValue(url, tag, className))
    print(titles)

    tag = 'span'
    # className = 'basicList_price__2r23_'
    className = "price_num__2WUXn"
    for url in url_list :
        prices.append(getNameValue(url, tag, className))
    print(prices)

    # context = {
    #     'titles':titles,
    #     'prices':prices
    # }

    # return context

getshop()