from urllib.request import urlopen
from urllib import parse
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


def imgcrawl(keyword):
    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    newUrl = url+quote_plus(keyword)
    img_src = ''
    count = 0
    html = urlopen(newUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    imglist = soup.find_all("img")
    for img in imglist:
        count += 1
        img_src = img['src']
        if count >= 2:
            break

    return img_src
