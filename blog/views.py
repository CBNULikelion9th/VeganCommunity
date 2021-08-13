from django.shortcuts import redirect, render
from .forms import  PostForm, ReportForm, SaveForm, AddForm
from .models import Post


# Create your views here.

def map_main(request):
    return render(request, 'blog/main.html')
def vegan_info(request):
    return render(request, 'blog/info.html')



def store_save(request):
    if request.method == 'GET':
        form = SaveForm()
    elif request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_main',)

    return render(request, 'blog/save.html',{
        'form':form,
    })

def area_report(request):
    if request.method == 'GET':
        form = ReportForm()
    elif request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_main')

    return render(request, 'blog/report.html',{
        'form':form,
    })


def vegan_area_add(request):
    if request.method == 'GET':
        form = PostForm()        
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_main',)

    return render(request,'blog/add.html',{
        'form':form,
    })


