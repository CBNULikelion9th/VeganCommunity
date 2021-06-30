from django.shortcuts import render
from .forms import PostForm, ReportForm
from .models import Post


# Create your views here.


def map_main(request):
    return render(request, 'blog/main.html')

def vegan_info(request):
    return render(request, 'blog/info.html')

def store_save(request):
    return render(request, 'blog/save.html')

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

