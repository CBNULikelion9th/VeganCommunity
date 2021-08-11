from urllib.request import urlopen
from urllib import parse
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
# from urllib.parse import quote
import ssl

def imgcrawl(keyword):
    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    newUrl = url+quote_plus(keyword)

    # context = ssl._create_unverified_context()

    html = urlopen(newUrl).read()
    soup = BeautifulSoup(html,'html.parser')
    img = soup.find("img")
    img_src = img.get("src")
    # img = soup.find_all('img', {"class":'_image'})
    # for i in img_src:
    print(img_src)
        # print()

    return img_src