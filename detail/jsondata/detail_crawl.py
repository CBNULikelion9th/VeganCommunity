from urllib.request import urlopen
from urllib import parse
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import ssl

def imgcrawl(keyword):
    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    newUrl = url+quote_plus(keyword)

    html = urlopen(newUrl).read()
    soup = BeautifulSoup(html,'html.parser')
    img = soup.find("img")
    img_src = img.get("src")


    return img_src