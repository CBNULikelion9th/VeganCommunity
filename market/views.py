from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm #CommentForm
from django.utils import timezone

def market_home(request):
    return render(request, 'market/home.html')


def farmer_notice(request):
    return render(request, 'market/farmer_notice.html')

def market_list(request):
    market_list = Post.objects.all()
    context = {
        'market_list': market_list,
    }
    return render(request, 'market/market_list.html', context)

def market_detail(request, post_id ):
    post = Post.objects.get(id=post_id)
    default_view_count = post.view_count
    post.view_count = default_view_count + 1
    post.save()
    return render(request, 'market/market_detail.html', {
        'post':post,
    })

def market_new(request):
    
    form = Post(request.POST, request.FILES )
    if request.method == 'GET':
        form = Post()
    
    elif request.method == 'POST':
        form = Post(request.POST, request.FILES)

        if form.is_valid():
            form.title = request.POST['title']
            form.writer = request.POST['writer']
            form.content = request.POST['content']
            form.image = request.POST['image']
            # form.organic =request.POST['organic']
        
            if 'organic' in request.POST:
                print ("유기농")
            else:
                form = Post()
                print (" ")  

            if 'nature' in request.POST:
                print ("자연농")
            else:
                form = Post()
                print (" ")   

            if 'usual' in request.POST:
                print ("일반농")
            else:
                form = Post()
                print (" ")   

            # if request.POST.has_key("organic"):
            market_new = Post.objects.create(
                title=title, writer=writer, content=content, image=image,
                )
            return redirect('market_detail', post_id=post.id)
            
    return render(request, 'market/market_new.html',{'form':form })

def market_create(request):
    new_post= Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.content = request.POST['content']

    if 'organic' in request.POST:
        print ('유기농')
    else:
        print (" ")  
        # return redirect('market_detail', post_id=new_post.id)
        # return None

    if 'nature' in request.POST:
        print ("자연농")
    else:
        print (" ") 

    if 'usual' in request.POST:
        print ("일반농")
    else:
        print (" ")   
        
    new_post.image = request.FILES['image']
    new_post.pub_date = timezone.now()
    new_post.save()
    return redirect('market_detail', new_post.id)

def market_edit(request, post_id):
    market_edit = Post.objects.get(id=post_id)
    
    if request.method == "POST":
        form = Post(request.POST, request.FILES, request.checkbox)
        if form.is_valid():
            form.title = request.POST['title']
            form.writer = request.POST['writer']
            form.content = request.POST['content']
            form.image = request.POST['image']

            if 'organic' in request.POST:
                print ("유기농")
            else:
                market_edit = Post()
                print (" ")  

            if 'nature' in request.POST:
                print ("자연농")
            else:
                market_edit = Post()
                print (" ")   

            if 'usual' in request.POST:
                print ("일반농")
            else:
                market_edit = Post()
                print (" ")   

            market_edit = form.save()
            market_edit = Post.objects.get(
                title=title, writer=writer, content=content, image=image, organic=organic, nature=nature, usual=usual
                )
            return redirect('market_detail', post_id=post.id)
    else:
        form = Post()            
        return render(request, 'market/market_edit.html', {
            'form':form,
            'post':market_edit,
        })

def market_update(request, post_id) :
    market_update = Post.objects.get(id = post_id)
    market_update.title = request.POST['title']
    market_update.writer = request.POST['writer']
    market_update.content = request.POST['content']
    market_update.image = request.FILES['image']

    if 'organic' in request.POST:
        print ("유기농")
    else:
        form = Post()
        print (" ")  

    if 'nature' in request.POST:
        print ("자연농")
    else:
        form = Post()
        print (" ")  
    if 'usual' in request.POST:
        print ("일반농")
    else:
        form = Post()
        print (" ")   

    market_update.pub_date = timezone.now()
    market_update.save()
    return redirect('market_detail', market_update.id)

def market_delete(request, post_id) :
    post = Post.objects.get (id=post_id)
    post.delete()
    return redirect('market_list')

def market_comment(request,  post_id):
    post = get_object_or_404(Post, pk=post_id)
    # post = Post.objects.get(id=post.id)#(post_id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('market_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'market/comment.html',{
        'form': form,
    })
