from django.shortcuts import render, redirect
from django.conf import settings
from urllib.request import Request, urlopen
from urllib.parse import urlencode, unquote, quote_plus
from urllib import parse
import urllib
import requests
import json

import urllib.request as ul
import xmltodict
from . import food_info
from . import foodapi
from .models import Ingredient, FoodNutrients, Products, ShoppingMall

def info(request):
    # result = food_info.info()
    # context ={
    #     'result_1' : result["response"]["body"]["items"]["item"][1]["RPRSNT_RAWMTRL_NM"],
    #     'result_2' : result["response"]["body"]["items"]["item"][0]["RPRSNT_RAWMTRL_NM"]
    # }
    category = Ingredient(f1="나물",f2="생선",f3="떡",f4="국",f5="면")
    result = foodapi.read_data()

    foodset = result["I2790"]["row"]
    index = [4]

    for i in range(0,3):
        if "닭" in foodset[i]["DESC_KOR"]:
            result_1=foodset[i]["DESC_KOR"]
            index.append(i)

    context ={
        'category':category,
        'index' : index,
        'result_1':result_1
    }
    
    return render(request,'detail/main.html',context)

def category1(request):
    # category = Ingredient.objects.get()
    category = Ingredient(f1="나물",f2="생선",f3="떡",f4="국",f5="면")
    # category.save()
    check=1
    if request.method == "POST":
        context = {
            'category':category,
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
            'check':check
        }
    return render(request,'detail/main.html',context)