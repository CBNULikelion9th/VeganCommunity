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
from .models import Vegan, Ingredient, Product, Shopping

def info(request):
    # result = food_info.info()
    # context ={
    #     'result_1' : result["response"]["body"]["items"]["item"][1]["RPRSNT_RAWMTRL_NM"],
    #     'result_2' : result["response"]["body"]["items"]["item"][0]["RPRSNT_RAWMTRL_NM"]
    # }
    
    return render(request,'detail/main.html')

def category1(request):
    category = Vegan.objects.get(pk=1)
    check=1
    if request.method == "POST":
        context = {
            'category':category,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category2(request):
    category = Ingredient.objects.get(pk=1)
    check=2
    if request.method == "POST":           
        context = {
            'category':category,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category3(request):
    category = Product.objects.get(pk=1)
    check=3
    if request.method == "POST":
        context = {
            'category':category,
            'check':check
        }
    return render(request,'detail/main.html',context)

def category4(request):
    category = Shopping.objects.get(pk=1)
    check=4
    if request.method == "POST": 
        context = {
            'category':category,
            'check':check
        }
    return render(request,'detail/main.html',context)