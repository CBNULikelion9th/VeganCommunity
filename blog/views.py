from django.shortcuts import render
from .forms import PostForm, ReportForm
from .models import Post


# Create your views here.

def post_map(request):
    return render(request, 'blog/map.html')

def post_main(request):
    return render(request, 'blog/main.html')

def post_info(request):
    return render(request, 'blog/info.html')

def post_save(request):
    return render(request, 'blog/save.html')

def post_report(request):
    if request.method == 'GET':
        form = ReportForm()

    return render(request, 'blog/report.html', {
        'form' : form,
    })

def post_add(request):
    if request.method == 'GET':
        form = PostForm()

    return render(request, 'blog/add.html', {
        'form' : form,
    })

