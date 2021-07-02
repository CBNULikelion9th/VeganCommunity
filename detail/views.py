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
from .models import Category

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# def main(request):
#     return render(request, 'detail/main.html')

def info(request):
    result = food_info.info()
    context ={
        'result' : result["response"]["body"]["items"]["item"][1]["RPRSNT_RAWMTRL_NM"]
    }
    
    return render(request,'detail/main.html', context)

def category(request, num):
    if request.method == "POST":
        if num == 1:
            category = Category.objects.get()

    return render(request,'detail/main.html')