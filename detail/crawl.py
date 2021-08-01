import requests as r
import urllib.request as ur

def crawling(item):
    apikey = "AIzaSyDG_htb8KLimgQvNbngBjYHL-Pv0vZQnUo"

    engineid = "e885abd5f563ddafb"

    url = "https://www.googleapis.com/customsearch/v1"

    param = {
        "key":apikey,

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


# import requests
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# from urllib.parse import quote_plus
# import urllib.request
# from urllib.error import URLError, HTTPError

# # keyword = []

# def openurl(url):
#     url = 'https://www.google.com/search?q='
#     try:
#         headers = {'User-Agent' : 'Chrome/66.0.3359.181'}
#         req = urllib.request.Request(url, headers=headers)
#         html = urllib.request.urlopen(req)
#     except HTTPError as e:
#         err = e.read()
#         code = e.getcode()

#     source = html.read()
#     html.close()
#     return source


# def crawling(item):
#     # keyword = item
#     # for item in filter_list:
#     #     keyword.append(item)
#     # url = 'https://www.google.com/search?q='
#     url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyDG_htb8KLimgQvNbngBjYHL-Pv0vZQnUo&cx=e885abd5f563ddafb&q='
#     Url = url + quote_plus(item)
#     # print(Url)
#     # driver = webdriver.Chrome("C:/Users/happy/Downloads/chromedriver_win32/chromedriver.exe")
#     # driver.get(url)
#     # driver.quit()
#     # time.sleep(1)
#     # req = requests.get(url)
#     html = openurl(Url)
#     print(1)
#     # print(html)

#     # html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     image = soup.find_all(class_='rg_i Q4LuWd')
#     print(2)
#     # print('number of img tags: ', len(images))
    
#     # for item in filter_list:
#     # my_titles = soup.select(
#     # 'h3 > a'
#     # )
#     print(image)
#     n = 1
#     for i in image:
#         imgUrl = i['data-source']
#         with urlopen(imgUrl) as f:
#             with open('C:/Users/happy/Desktop/vegan/VeganCommunity/detail/static/img/' + item +'.jpg','wb') as h: # w - write b - binary
#                 img = f.read()
#                 h.write(img)
#                 print('다운로드 완료')
#         n += 1
#         if n > 1:
#             break   
#     # n = 1
#     # print(image)
#     # for i in image:
#     #     try:
#     #         imgUrl = i["src"]
#     #     except:
#     #         imgUrl = i["data-src"]
#     #     with urllib.request.urlopen(imgUrl) as f:
#     #         with open('C:/Users/happy/Desktop/vegan/VeganCommunity/detail/static/img/' + item + '.jpg', 'wb') as h:
#     #             img = f.read()
#     #             h.write(img)
#     #     n += 1
#     #     if n > 1:
#     #         break
#     # driver.quit()

