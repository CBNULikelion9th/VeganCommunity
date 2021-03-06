from django.shortcuts import render
from django.conf import settings
import urllib.request as ul
# from . import foodapi
from .models import Ingredient, FoodNutrients, Products, ShoppingMall
from . import crawl
from urllib.request import urlopen
# from bs4 import BeautifulSoup
import random
from .jsondata.cate1_data import food_list_set
from .jsondata.cate2_data import filter_list2
from .jsondata.cate3_data import filter_list3
from .jsondata.detail_crawl import imgcrawl
from random import shuffle

index = []      # 해당 음식의 인덱스
food_list = food_list_set   # api로 가져온 전체 음식리스트
# check=1         # 카테고리 구분
filter_list1 = ["비건", "건강식품", "식품성분"]  # 필터링 요소에 따른 음식리스트
imglink = []
filter_list = []


def info(request):
    category = Ingredient(f1="나물", f2="구이", f3="떡",
                          f4="국", f5="면")  # 처음엔 카테고리 1을 보여줌
    check = 1

    context = {
        'category': category,
        # 'index' : index,
        'filter_list': filter_list1,
        'check': check
    }

    return render(request, 'detail/main.html', context)


def category1(request):
    category = Ingredient(f1="나물", f2="구이", f3="떡", f4="국", f5="면")

    check = 1
    if request.method == "POST":
        context = {
            'category': category,
            'index': index,
            'filter_list': filter_list1,
            'check': check
        }
    return render(request, 'detail/main.html', context)


def category2(request):
    category = FoodNutrients(f1="열량", f2="탄수화물", f3="단백질",
                             f4="지방", f5="당류", f6="콜레스테롤")
    check = 2
    if request.method == "POST":
        context = {
            'category': category,
            'index': index,
            'filter_list2': filter_list1,
            'check': check
        }
    return render(request, 'detail/main.html', context)


def category3(request):
    category = Products(f1="채소류", f2="과일류", f3="곡류")
    check = 3
    if request.method == "POST":
        context = {
            'category': category,
            'index': index,
            'filter_list': filter_list1,
            'check': check
        }
    return render(request, 'detail/main.html', context)


def category4(request):
    category = ShoppingMall(f1="마켓컬리", f2="쿠팡", f3="푸드슈퍼마켓", f4="G마켓")
    check = 4
    if request.method == "POST":
        context = {
            'category': category,
            'index': index,
            'filter_name': filter_list1,
            'check': check
        }
    return render(request, 'detail/main.html', context)


def filter(request, check):
    filter_list1.clear()
    imglink.clear()
    if request.method == "POST":
        selected = request.POST.getlist('selected[]')

        if check == 1:
            category = Ingredient(f1="나물", f2="구이", f3="떡", f4="국", f5="면")
            shuffle(food_list)
            while len(filter_list1) < 3:
                for item in selected:
                    for i in range(1, len(food_list)):
                        if item in food_list[i]:
                            if food_list[i] not in filter_list1:
                                # 필터링값에 따라 보여줄 리스트
                                filter_list1.append(food_list[i])
                                break

            for item in filter_list1:
                imglink.append(str(crawl.crawling(item)))   # 이미지 크롤링
            context = {
                'category': category,
                'filter_list': filter_list1,
                'check': check,
                'imglink': imglink,
            }

        elif check == 2:
            from .jsondata.cate2_data import filter_list2
            shuffle(filter_list2)
            filter_check = []
            category = FoodNutrients(
                f1="열량", f2="탄수화물", f3="단백질", f4="지방", f5="당류", f6="콜레스테롤")
            for item in selected:
                if item == "열량":
                    filter_check.append(1)
                if item == "탄수화물":
                    filter_check.append(2)
                if item == "단백질":
                    filter_check.append(3)
                if item == "지방":
                    filter_check.append(4)
                if item == "당류":
                    filter_check.append(5)
                if item == "콜레스테롤":
                    filter_check.append(6)
            context = {
                'check': check,
                'category': category,
                'filter_check': filter_check,
                'filter_list2': filter_list2,
            }

        elif check == 3:
            from .jsondata.detail_crawl import imgcrawl
            imglink.clear()
            filter_list.clear()
            filter_check = []
            category = Products(f1="채소류", f2="과일류", f3="곡류")

            for item in selected:
                if item == "채소류":
                    filter_check.append(1)
                    filter = filter_list3[0][random.randrange(1, 8)]
                    filter_list.append(filter)
                    imglink.append(str(imgcrawl(filter)))
                if item == "과일류":
                    filter_check.append(2)
                    filter = filter_list3[1][random.randrange(1, 7)]
                    filter_list.append(filter)
                    imglink.append(str(imgcrawl(filter)))
                if item == "곡류":
                    filter_check.append(3)
                    filter = filter_list3[2][random.randrange(1, 7)]
                    filter_list.append(filter)
                    imglink.append(str(imgcrawl(filter)))

            while len(filter_list) < 3:
                for filter in filter_check:
                    filter = filter_list3[filter-1][random.randrange(1, 7)]
                    filter_list.append(filter)
                    imglink.append(str(imgcrawl(filter)))

            context = {
                'check': check,
                'category': category,
                'filter_check': filter_check,
                'imglink': imglink,
                'filter_list': filter_list,
            }

        elif check == 4:
            from .jsondata.cate4_data import titles, prices, getshop
            getshop()

            filter_check = []
            filter_name = []
            category = ShoppingMall(f1="마켓컬리", f2="쿠팡", f3="푸드슈퍼마켓", f4="G마켓")
            for item in selected:
                if item == "마켓컬리":
                    filter_check.append(1)
                    filter_name.append("마켓컬리")
                if item == "쿠팡":
                    filter_check.append(2)
                    filter_name.append("쿠팡")
                if item == "푸드슈퍼마켓":
                    filter_check.append(3)
                    filter_name.append("푸드슈퍼마켓")
                if item == "G마켓":
                    filter_check.append(4)
                    filter_name.append("G마켓")
            if len(filter_check) < 3:
                filter_name.append(item)
                filter_name.append(item)

            sample = []
            for item in filter_check:
                sample.append(random.sample(titles[item-1], 1))
            if len(sample) < 2:
                sample.append(random.sample(titles[2], 1))
                sample.append(random.sample(titles[3], 1))
            elif len(sample) < 3:
                sample.append(random.sample(titles[3], 1))

            context = {
                'check': check,
                'category': category,
                'filter_check': filter_check,
                'sample': sample,
                'prices': prices,
                'filter_name': filter_name
            }
            return render(request, 'detail/main.html', context)

    return render(request, 'detail/main.html', context)


def detail_info(request, check):
    # url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
    imglist = []
    if check == 1:
        for filter in filter_list1:
            imglist.append(imgcrawl(filter))
        context = {
            'check': check,
            'filter_list': filter_list1,
            'imglist': imglist
        }
    elif check == 2:
        for filter in filter_list2:
            imglist.append(imgcrawl(filter['name']))

        context = {
            'check': check,
            'filter_list2': filter_list2,
            'imglist': imglist
        }
    elif check == 3:
        for filter in filter_list:
            imglist.append(imgcrawl(filter))

        context = {
            'check': check,
            'filter_list': filter_list,
            'imglist': imglist
        }

    return render(request, 'detail/info.html', context)


def search(request):
    from .calc_crwal import calc
    keyword = ''
    imgsrc = ''

    if request.method == "POST":
        keyword = request.POST.get('keyword')
        imgsrc = imgcrawl(keyword)
        calclist = calc(keyword)

    context = {
        'keyword': keyword,
        'imgsrc': imgsrc,
        'calclist': calclist,
    }

    return render(request, 'detail/search.html', context)
