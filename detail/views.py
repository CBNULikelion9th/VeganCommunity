from django.shortcuts import render, redirect
from django.conf import settings
import urllib.request as ul
from . import foodapi
from .models import Ingredient, FoodNutrients, Products, ShoppingMall
from . import crawl
from urllib.request import urlopen
from bs4 import BeautifulSoup

index = []      # 해당 음식의 인덱스
food_list= []   # api로 가져온 전체 음식리스트
# check=1         # 카테고리 구분
filter_list1=["더덕구이", "도미구이","병어구이"]  # 필터링 요소에 따른 음식리스트
imglink = []

result = foodapi.read_data()    # json 읽어옴
foodset = result["I2790"]["row"]
for i in range(0,len(result["I2790"]["row"])):
    # for i in range(0,len(temp)):
    food_list.append(foodset[i]["DESC_KOR"])
    # food_list.append(foodset[i])
    index.append(i)
    print(food_list)

def info(request):
    category = Ingredient(f1="나물",f2="구이",f3="떡",f4="국",f5="면")  # 처음엔 카테고리 1을 보여줌
    # result = foodapi.read_data()    # json 읽어옴
    # foodset = result["I2790"]["row"]
    check=1 
    # for i in range(0,len(result["I2790"]["row"])):
    #     food_list.append(foodset[i]["DESC_KOR"])
    #     index.append(i)
    # print(food_list)
    context ={
        'category':category,
        'index' : index,
        'food_list':food_list,
        'check':check
    }
    
    return render(request,'detail/main.html',context)

def category1(request):
    # category = Ingredient.objects.get()
    category = Ingredient(f1="나물",f2="구이",f3="떡",f4="국",f5="면")
    # category.save()
    check=1
    if request.method == "POST":
        context = {
            'category':category,
            'index' : index,
            'food_list':food_list,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category2(request):
    # category = FoodNutrients.objects.get()
    category =  FoodNutrients(f1="열량",f2="탄수화물",f3="단백질",f4="지방",f5="당류",f6="콜레스테롤")
    check=2
    if request.method == "POST":           
        context = {
            'category':category,
            'index' : index,
            'food_list':food_list,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category3(request):
    # category = Products.objects.get()
    category = Products(f1="채소류",f2="과일류",f3="곡류")
    check=3
    if request.method == "POST":
        context = {
            'category':category,
            'index' : index,
            'food_list':food_list,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category4(request):
    # category = ShoppingMall.objects.get()
    category = ShoppingMall(f1="마켓컬리",f2="쿠팡",f3="푸드슈퍼마켓",f4="G마켓")
    check=4
    if request.method == "POST": 
        context = {
            'category':category,
            'index' : index,
            'food_list':food_list,
            'check':check
        }
    return render(request,'detail/main.html',context)

def filter(request, check):    
    filter_list1.clear()
    imglink.clear()
    if request.method == "POST":
        selected = request.POST.getlist('selected[]')
        # print(selected)

        if check == 1:
            category = Ingredient(f1="나물",f2="구이",f3="떡",f4="국",f5="면")
        
            for item in selected:
                print(food_list)
                for i in range(1,len(food_list)):    
                    if item in food_list[i]:        # selected로부터 선택된 item이 전체리스트에 있을 경우
                        print(type(food_list))
                        filter_list1.append(food_list[i]) # 필터링값에 따라 보여줄 리스트

            print(filter_list1)
            for item in filter_list1:
                print(1)
                imglink.append(str(crawl.crawling(item)))   # 이미지 크롤링
            context = {
                'category':category,
                'filter_list':filter_list1,
                'check':check,
                'imglink' : imglink,
            }
            print(imglink)

        elif check == 2:
            from .jsondata.cate2_data import filter_list2
            print(2)
            print(filter_list2)
            filter_check = []
            category =  FoodNutrients(f1="열량",f2="탄수화물",f3="단백질",f4="지방",f5="당류",f6="콜레스테롤")
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
                'check':check,
                'category':category,
                'filter_check':filter_check,
                'filter_list2':filter_list2,
            }

        elif check == 3:
            from .jsondata.cate3_data import filter_list2
            print(3)
            print(selected)
            print(filter_list2)
            
            filter_check = []
            category =  Products(f1="채소류",f2="과일류",f3="곡류")
            for item in selected:
                if item == "채소류":
                    filter_check.append(1)
                if item == "과일류":
                    filter_check.append(2)
                if item == "곡류":
                    filter_check.append(3)
            context = {
                'check':check,
                'category':category,
                'filter_check':filter_check,
                'filter_list2':filter_list2,
            }

        elif check == 4:
            # from .jsondata.cate4_data import filter_list2
            print(4)
            print(filter_list2)
            filter_check = []
            category =  ShoppingMall(f1="마켓컬리",f2="쿠팡",f3="푸드슈퍼마켓",f4="G마켓")
            for item in selected:
                if item == "마켓컬리":
                    filter_check.append(1)
                if item == "쿠팡":
                    filter_check.append(2)
                if item == "푸드슈퍼마켓":
                    filter_check.append(3)
                if item == "G마켓":
                    filter_check.append(4)
            print(filter_check)
            context = {
                'check':check,
                'category':category,
                'filter_check':filter_check,
                'filter_list2':filter_list2,
            }


    return render(request,'detail/main.html',context)

def getshop(request):
    from .jsondata.cate4_data import url_list, getClassValue, getNameValue

    titles = []
    tag = 'a'
    className = 'basicList_link__1MaTN'
    for url in url_list :
        titles.append(getClassValue(url, tag, className))
    print(titles)

    prices = []
    tag = 'span'
    # className = 'basicList_price__2r23_'
    className = "price_num__2WUXn"
    for url in url_list :
        prices.append(getNameValue(url, tag, className))
    print(prices)

    return render(request, 'detail/main.html')