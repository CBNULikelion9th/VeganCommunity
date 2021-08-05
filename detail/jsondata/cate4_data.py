from urllib.request import urlopen
from bs4 import BeautifulSoup

filter_list2 = []
price_list = []

url_list = [
    "https://search.shopping.naver.com/search/all?query=%EB%A7%88%EC%BC%93%EC%BB%AC%EB%A6%AC&frm=NVSHATC&prevQuery=%EC%8B%9D%EB%A3%8C%ED%92%88",
    "https://search.shopping.naver.com/search/all?query=%EC%BF%A0%ED%8C%A1%20%EB%B0%98%EC%B0%AC&frm=NVSHATC&prevQuery=%EC%BF%A0%ED%8C%A1",
    "https://search.shopping.naver.com/search/all?query=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93&frm=NVSHATC&prevQuery=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93%20%EB%B0%98%EC%B0%AC",
    "https://search.shopping.naver.com/search/all?query=G%EB%A7%88%EC%BC%93%20%EB%B0%98%EC%B0%AC&frm=NVSHATC&prevQuery=%ED%91%B8%EB%93%9C%EC%8A%88%ED%8D%BC%EB%A7%88%EC%BC%93"
]

def getClassValue(url, tag, className):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.find_all(tag,{"class", className})
    # print(content)
    for i in content:
        filter_list2.append(i['title'])
    print(filter_list2)
    return filter_list2

def getNameValue(url, tag, className) :
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    content = bs.find_all(tag, {"class": className})
    # print(content.get_text())
    for i in content:
        price_list.append(i.get_text())
    print(price_list)
    return price_list