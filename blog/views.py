from django.shortcuts import render
from .forms import PostForm, ReportForm, SaveForm
from .models import Post


# Create your views here.


def map_main(request):
    return render(request, 'blog/main.html')

def test(request):
    return render(request, 'blog/test.html')

def vegan_info(request):
    return render(request, 'blog/info.html')



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


def store_save(request):
    if request.method == 'GET':
        form = SaveForm()

        return render(request, 'blog/save.html', {
           'form' : form,
    })

