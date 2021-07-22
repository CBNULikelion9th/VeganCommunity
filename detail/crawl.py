import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# keyword = []

def crawling(item):
    keyword = item
    # for item in filter_list:
    #     keyword.append(item)
    url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712'.format(keyword)

    driver = webdriver.Chrome("C:/Users/happy/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get(url)
    driver.quit()
    # time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

    # print('number of img tags: ', len(images))
    
    # for item in filter_list:
    n = 1
    for i in images:
        try:
            imgUrl = i["src"]
        except:
            imgUrl = i["data-src"]
        with urllib.request.urlopen(imgUrl) as f:
            with open('C:/Users/happy/Desktop/vegan/VeganCommunity/detail/static/img/' + item + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
        if n > 1:
            break
    # driver.quit()