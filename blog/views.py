from django.shortcuts import render
from .forms import PostForm, ReportForm
from .models import Post


# Create your views here.


def map_main(request):
    return render(request, 'blog/main.html')

def search(request):
    return render(request, 'blog/search.html')

def vegan_info(request):
    return render(request, 'blog/info.html')

def store_save(request):
    return render(request, 'blog/save.html')

def exception(request):
    return render(request, 'blog/exception.html')

def mypage(request):
    return render(request, 'blog/mypage.html')

def area_report(request):
    if request.method == 'GET':
        form = ReportForm()

        return render(request, 'blog/report.html', {
           'form' : form,
    })
def vegan_area_add(request):
    if request.method == 'GET':
        form = PostForm()

        return render(request, 'blog/add.html', {
           'form' : form,
    })



#여누
def store_1(request):
    return render(request, 'blog/store_1.html')
#오프리
def store_2(request):
    return render(request, 'blog/store_2.html')
#늘푸른식당
def store_3(request):
    return render(request, 'blog/store_3.html')
#스토리
def store_4(request):
    return render(request, 'blog/store_4.html')
#하일
def store_5(request):
    return render(request, 'blog/store_5.html')
#러빙헛
def store_6(request):
    return render(request, 'blog/store_6.html')
#비건바닐라
def store_7(request):
    return render(request, 'blog/store_7.html')
#세이비건
def store_8(request):
    return render(request, 'blog/store_8.html')
#에이블리
def store_9(request):
    return render(request, 'blog/store_9.html')
#채식주의자의무화과
def store_10(request):
    return render(request, 'blog/store_10.html')