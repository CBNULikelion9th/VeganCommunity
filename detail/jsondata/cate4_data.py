from urllib.request import urlopen
from bs4 import BeautifulSoup
# import urllib.request

titles = []
prices = []
# imgs = []

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

# def getImgValue(url, tag, className):
#     img_list = []
#     html = urlopen(url)
#     bs = BeautifulSoup(html, "html.parser")
#     content = bs.find(tag, class_= className)
#     # print(content.get_text())
#     # for i in content:
#     img_url = content.find("img")["src"]
#     # print(img_list)
#     return img_url

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

    # tag =  'a'
    # className = 'thumbnail_thumb__3Agq6'
    # for url in url_list :
    #     imgs.append(getImgValue(url, tag, className))
    # print(imgs)


# def getimg():
#     url = "https://search.shopping.naver.com/search/all?query=%EC%BF%A0%ED%8C%A1%20%EB%B0%98%EC%B0%AC&frm=NVSHATC&prevQuery=%EC%BF%A0%ED%8C%A1"
#     fp = urllib.request.urlopen(url)
#     source = fp.read();
#     fp.close()

#     #소스에서 img_area 클래스 하위의 소스를 가져온다.
#     soup = BeautifulSoup(source, 'html.parser')
#     soup = soup.find("div",class_ = "thumbnail_thumb_wrap__1pEkS _wrapper")
#     print(soup)
#     #이미지 경로를 받아온다.
#     imgURL = soup.find("img")["src"]

#     print(imgURL)


# getimg()
# getshop()