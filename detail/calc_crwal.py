from urllib.request import urlopen
from urllib import parse
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import re


def calc(keyword):
    url = "https://www.fatsecret.kr/%EC%B9%BC%EB%A1%9C%EB%A6%AC-%EC%98%81%EC%96%91%EC%86%8C/%EC%9D%BC%EB%B0%98%EB%AA%85/"
    newUrl = url+quote_plus(keyword)
    html = urlopen(newUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    calclist = soup.find_all(
        attrs={'class': 'nutrition_facts international'})
    body = ''
    try:
        body = re.sub('<.+?>', '', str(calclist[0]), 0, re.I | re.S)
    except IndexError:
        body = "해당 식품 정보가 존재하지 않습니다."
    return body
